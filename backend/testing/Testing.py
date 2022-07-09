import sys
import os
sys.path.append(os.environ.get("BACKEND_PATH"))

import Params
import DataLayer
import pickle
import MlLayer
import pandas as pd
from pymongo import MongoClient

#f = open('./test_data.json')
#test_json = json.load(f)
#with open('outfile', 'wb') as fp:
#    pickle.dump(data['items'], fp)

import DataLayer
import MlLayer

class Testing():
    def __init__(self):
        self.ml_layer = MlLayer.MlLayer()
        self.data_layer = DataLayer.DataLayer()

    def testFeedback(self, video_id, distractful):
        self.data_layer.store_feedback(video_id, distractful)

testing = Testing()
testing.testFeedback("jWkH6K4_xEg", True)