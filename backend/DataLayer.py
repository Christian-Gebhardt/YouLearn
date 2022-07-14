"""
Handle data transfers
"""

from curses import meta
from os import system
import Utils
import Helpers
import pandas as pd
import pickle
import Params

class DataLayer():
    def __init__(self):
        self.load_db()
        self.load_kaggle()
        self.load_feedbacks()

    def load_db(self):
        self.db = Helpers.get_db()

    def load_kaggle(self):
        train_col = self.db['training_col']
        df = pd.DataFrame(list(train_col.find().limit(Params.DB_LIMIT)))
        self.dataset_kaggle = df

    def load_feedbacks(self):
        self.collection_feedbacks = self.db['feedbacks']
        df = pd.DataFrame(list(self.collection_feedbacks.find().limit(Params.DB_LIMIT)))
        self.dataset_feedbacks = df

    def store_feedback(self, video_id, is_distractful):
        metadata = self.get_metadata(video_id)['items'][0]
       
        to_insert = { 
                'video_id' : metadata['id'], 
                'title' : metadata['snippet']['title'], 
                'description' : metadata['snippet']['description'], 
                'category_id' : int(not is_distractful)
            }
        
        self.collection_feedbacks.insert_one(to_insert)

    def load_trained_model(self):
        '''
        Method tries to load the dynamic model, if not possible, fallback to the static model.
        '''
        try:
            return pickle.load(open(Params.PATH_TO_DYNAMIC_MODEL, 'rb'))
        except Exception as e:
            print("Failed to load the dynamic model! Fallback to static model.")

        try:
            return pickle.load(open(Params.PATH_TO_STATIC_MODEL, 'rb'))
        except Exception as e:
            print("Failed to load the static model! ")

        exit()
        
    def get_metadata(self, videos_ids):
        # Returns json containing metadata of videos from their ids
        return Helpers.get_yt_client().videos().list(id=videos_ids, part="snippet").execute()

    def get_df_to_predict(self, videos_metadata):
        # Returns dataframe which contains video id and text to be passed to ml model
        df = pd.DataFrame(columns=['video_id', 'to_predict'])

        for index in range(len(videos_metadata)):
            df.loc[len(df)] = [videos_metadata[index]['id'], videos_metadata[index]['snippet']['title'] + " " + videos_metadata[index]['snippet']['description']]

        return df

    def store_model(self, model):
        filehandler = open(Params.PATH_TO_DYNAMIC_MODEL, 'wb') 
        pickle.dump(model, filehandler)
        print('Retraining finished')    
