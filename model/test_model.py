from sklearn import svm
from sklearn import metrics
from sklearn import cross_validation
import pandas as pd
import numpy as np
from sklearn.externals import joblib

test_df = pd.read_csv( 'test_label.csv' )
features_t = np.array([test_df['x'].tolist(),
                       test_df['y'].tolist(),
                       test_df['num_digit'].tolist(),
                       test_df['num_ja'].tolist(),
                       ], np.float64)
labels_t = np.array(test_df['label'])
features_t = features_t.T

clf = joblib.load('model/clf.pkl') 

print(clf.predict(features_t))
