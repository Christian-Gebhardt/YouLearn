"""
Handle data transfers
"""

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
        self.ids_feedbacks = df

    def store_feedback(self, video_id, feedback):
        # TODO

        # 1. Get metadata
        metadata = self.get_metadata(video_id)
        
        # 2. Add column if distractful

        # 3. Insert to collection

        return None

    def feedbacks_ids_to_feedbacks_df(self, ids_feedbacks):
        # Input - feedbacks as stored in mongo
        # Output - df in format as training collection

        return None

    def load_trained_model(self):
        # Returns trained ml model
        try:
            return pickle.load(open(Params.PATH_TO_TRAINED_MODEL_MLP, 'rb'))
        except FileNotFoundError:
            print("Failed to load the trained model!")
        
    def get_metadata(self, videos_ids):
        # Returns json containing metadata of videos from their ids
        return Helpers.get_yt_client().videos().list(id=videos_ids, part="snippet").execute()

    def get_df_to_predict(self, videos_metadata):
        # Returns dataframe which contains video id and text to be passed to ml model
        df = pd.DataFrame(columns=['video_id', 'to_predict'])

        for index in range(len(videos_metadata)):
            df.loc[len(df)] = [videos_metadata[index]['id'], Utils.remove_punctuation(videos_metadata[index]['snippet']['title']) + " " + Utils.remove_punctuation(videos_metadata[index]['snippet']['description'])]

        return df

    def store_model(self, model):
        filehandler = open('./models/mlp.sav', 'w') 
        pickle.dump(model, filehandler)

    
