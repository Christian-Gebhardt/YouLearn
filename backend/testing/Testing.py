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

with open (os.environ.get("BACKEND_PATH")+'/testing/outfile', 'rb') as fp:
    metadata = pickle.load(fp)

df_to_predict = DataLayer.get_df_to_predict(metadata)
distractful_ids = MlLayer.ml_filter_distractful(df_to_predict)

print(distractful_ids)
