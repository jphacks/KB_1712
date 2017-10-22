from sklearn.externals import joblib
from PIL import Image
import pandas as pd
import numpy as np
import unicodedata
import json
import os

def merge_block(head_block, block_list):
    guide_text = head_block["description"].split("\n")
    guide_text_index = 0

    merged_block_list = []
    temp_block_list = []
    check_text = ""

    for block in block_list:
        check_text += block["description"]
        temp_block_list.append(block)

        if check_text == guide_text[guide_text_index].replace(' ',''):
            merged_block_list.append({'boundingPoly': {'vertices': [temp_block_list[0]["boundingPoly"]["vertices"][0],\
            temp_block_list[-1]["boundingPoly"]["vertices"][1],\
            temp_block_list[-1]["boundingPoly"]["vertices"][2],\
            temp_block_list[0]["boundingPoly"]["vertices"][3]]},\
          'description': check_text})
            check_text = ""
            temp_block_list = []
            guide_text_index += 1
            
    return merged_block_list

def translate_to_plot_box(block_list):
    return [{"x" : block["boundingPoly"]["vertices"][0]["x"], \
                 "y" : block["boundingPoly"]["vertices"][0]["y"], \
                "w" : block["boundingPoly"]["vertices"][2]["x"] - block["boundingPoly"]["vertices"][0]["x"], \
                "h" : block["boundingPoly"]["vertices"][2]["y"] - block["boundingPoly"]["vertices"][0]["y"], \
                } for block in block_list]

def plot_reciept(image_path, box_list):
    im = np.array(Image.open(image_path), dtype=np.uint8)

    # Create figure and axes
    fig,ax = plt.subplots(1)
    fig.set_size_inches(20, 10)

    # Display the image
    ax.imshow(im)

    # Create a Rectangle patch
    for box in box_list:
        rect = patches.Rectangle((box["x"],box["y"]),box["w"],box["h"],linewidth=1,edgecolor='r',facecolor='none')
        # Add the patch to the Axes
        ax.add_patch(rect)

    plt.show()
    
def get_un_count(sentence,target_type):
    return [unicodedata.name(ch).split(" ")[0] for ch in sentence].count(target_type)

def translate_train_data(head_block, block_list):
    un_ja_types = ["CJK", "HIRAGANA", "KATAKANA"]
    un_digit_types = ["DIGIT"]

    return [{"x": (block["boundingPoly"]["vertices"][0]["x"] - head_block["boundingPoly"]["vertices"][0]["x"]) / head_block["boundingPoly"]["vertices"][1]["x"],\
                   "y": (block["boundingPoly"]["vertices"][0]["y"] - head_block["boundingPoly"]["vertices"][0]["y"]) / head_block["boundingPoly"]["vertices"][2]["y"],\
                   "num_ja": sum([get_un_count(block["description"], types) for types in un_ja_types]) / len(block["description"]),\
                   "num_digit": sum([get_un_count(block["description"], types) for types in un_digit_types]) / len(block["description"]),\
                    "description": block["description"]\
                  } for block in block_list]

def get_train_data(json_file):
    head_block, content_block_list = json_file[0], json_file[1:]
    merged_block_list = merge_block(head_block, content_block_list)
    return translate_train_data(head_block, merged_block_list)

def convert_price(price):
    return int("".join([c for c in price if unicodedata.name(c).split(' ')[0] == "DIGIT"]))

def parse_info(result):
    date = result[result["label"] == "date"]["description"].tolist()[0]
    product = result[result["label"] == "product"]
    price = result[result["label"] == "price"]
    cleared_price = [ convert_price(price[ abs(price["y"] - product_y) < 0.005]["description"].tolist()[0]) for product_y in product["y"] ]
    
    return [{"date" : date, "product" : pro, "price" : pri} for pro, pri in zip(product["description"], cleared_price)]
    

def predict_receipt(responses_json_path, model_path):
    responses_json = json.load(open(responses_json_path, 'r'))
    responses_df = pd.DataFrame([data for data in get_train_data(responses_json["responses"][0]["textAnnotations"])])

    features_test = np.array([responses_df['x'].tolist(),responses_df['y'].tolist(),\
    responses_df['num_digit'].tolist(),responses_df['num_ja'].tolist()], np.float64)
    features_test = features_test.T

    clf = joblib.load(model_path)
    predict_result = clf.predict(features_test)
    
    merged_result = pd.DataFrame([responses_df["description"],responses_df["x"],responses_df["y"] ,predict_result]).T
    merged_result.columns = ['description', 'x', 'y', 'label']
    
    return parse_info(merged_result)