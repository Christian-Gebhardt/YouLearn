import sys
import os
sys.path.append(os.environ.get("BACKEND_PATH"))

import DataLayer
import pickle
import MlLayer
import pandas as pd

#f = open('./test_data.json')
#test_json = json.load(f)
#with open('outfile', 'wb') as fp:
#    pickle.dump(data['items'], fp)

def testGetDistractful(metadata):
   
    # 2. Create df with video_id and value to predict from the metadata
    df_to_predict = DataLayer.get_df_to_predict(metadata)

    # 3. Call to ml layer to get the ids of the distractful videos
    model = DataLayer.get_trained_model()
    distractful_ids = MlLayer.ml_filter_distractful(model, df_to_predict)

    print(distractful_ids)

def testSort(metadata):
   
     # 2. Create df with video_id and value to predict from the metadata
    df_to_predict = DataLayer.get_df_to_predict(metadata)

    # 3. Call to ml layer to get the ids of the distractful videos
    model = DataLayer.get_trained_model()
    distractful_ids = MlLayer.ml_filter_and_sort_distractful(model, df_to_predict)

    print(distractful_ids)

with open (os.environ.get("BACKEND_PATH")+'/testing/outfile', 'rb') as fp:
    metadata = pickle.load(fp)

testSort(metadata)