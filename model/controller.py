import request_api
import analysis_receipt
import controll_camera

# controll_camera.get_image("image/photo.jpg")
request_api.call_vision_api("input_file.txt")
print(analysis_receipt.predict_receipt("output/respone.json", "model/clf.pkl"))