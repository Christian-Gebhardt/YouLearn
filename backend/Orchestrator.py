"""
Orchestrator to handle calls from endpoint (so they won't go directly to data layer or ml layer)
"""

import DataLayer
import MlLayer

def filter_distractful(recommended_videos_ids):
    # Method called by endpoint to filter distractful videos

    # 1. Get metadata of the videos from youtube API
    metadata = DataLayer.get_metadata(recommended_videos_ids)
 
    # 2. Create df with video_id and value to predict from the metadata
    df_to_predict = DataLayer.get_df_to_predict(metadata['items'])

    # 3. Call to ml layer to get the ids of the distractful videos
    model = DataLayer.get_trained_model()
    distractful_ids = MlLayer.ml_filter_distractful(model, df_to_predict)
  
    return distractful_ids

def feedback(video_id, feedback):
    # TODO
    if feedback:
        return video_id+" was distractful"
    else:
        return video_id+" wasn't distractful"

def get_recommendations(userId, video_url):
    # TODO
    return None