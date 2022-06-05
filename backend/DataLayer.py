"""
Handle data transfers
"""

import HelperFunctions
import Helpers
import pandas as pd
import numpy as np
import pickle
import Params

def get_trained_model():
    # Returns trained ml model
    return pickle.load(open(Params.PATH_TO_TRAINED_MODEL_MLP, 'rb'))

def get_metadata(recommended_videos_ids):
    # Returns json containing metadata of videos from their ids
    return Helpers.get_yt_client().videos().list(id=recommended_videos_ids, part="snippet").execute()

def get_df_to_predict(videos_metadata):
    # Returns dataframe which contains video id and text to be passed to ml model

    df = pd.DataFrame(columns=['video_id', 'to_predict'])

    for index in range(len(videos_metadata)):
        df.loc[len(df)] = [videos_metadata[index]['id'], HelperFunctions.remove_punctuation(videos_metadata[index]['snippet']['title']) + " " + HelperFunctions.remove_punctuation(videos_metadata[index]['snippet']['description'])]

    return df