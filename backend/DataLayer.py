"""
Handle data transfers
"""

import Utils
import Helpers
import pandas as pd
import pickle
import Params

def get_trained_model():
    # Returns trained ml model
    try:
        return pickle.load(open(Params.PATH_TO_TRAINED_MODEL_MLP, 'rb'))
    except FileNotFoundError:
        print("Failed to load the trained model!")
    
def get_metadata(recommended_videos_ids):
    # Returns json containing metadata of videos from their ids
    return Helpers.get_yt_client().videos().list(id=recommended_videos_ids, part="snippet").execute()

def get_df_to_predict(videos_metadata):
    # Returns dataframe which contains video id and text to be passed to ml model

    df = pd.DataFrame(columns=['video_id', 'to_predict'])

    for index in range(len(videos_metadata)):
        df.loc[len(df)] = [videos_metadata[index]['id'], Utils.remove_punctuation(videos_metadata[index]['snippet']['title']) + " " + Utils.remove_punctuation(videos_metadata[index]['snippet']['description'])]

    return df