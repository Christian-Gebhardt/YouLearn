"""
Orchestrator to handle calls from endpoint (so they won't go directly to data layer or ml layer)
"""

import DataLayer
import MlLayer

class Orchestrator():
    def __init__(self):
        self.ml_layer = MlLayer.MlLayer()
        self.data_layer = DataLayer.DataLayer()

    def filter_distractful(self, recommended_videos_ids):
        # Method called by endpoint to filter distractful videos

        # 1. Get metadata of the videos from youtube API
        metadata = self.data_layer.get_metadata(recommended_videos_ids)
    
        # 2. Create df with video_id and value to predict from the metadata
        df_to_predict = self.data_layer.get_df_to_predict(metadata['items'])

        # 3. Call to ml layer to get the ids of the distractful videos
        distractful_ids = self.ml_layer.ml_filter_distractful(df_to_predict)

        return distractful_ids

    def filter_and_sort_distractful(self, filter_thershold, recommended_videos_ids):
        # Method called by endpoint to filter distractful videos

        # 1. Get metadata of the videos from youtube API
        metadata = self.data_layer.get_metadata(recommended_videos_ids)
    
        # 2. Create df with video_id and value to predict from the metadata
        df_to_predict = self.data_layer.get_df_to_predict(metadata['items'])

        # 3. Call to ml layer to get the sorted ids of recommended videos
        distractful_ids = self.ml_layer.ml_filter_and_sort_distractful(filter_thershold, df_to_predict)
    
        return distractful_ids

    def feedback(self, video_id, feedback):

        # TODO Decide if feedbacks stored as ids or as kaggle dataset -> adjust mongo sample

        # Store the feedback in the db collection feedback
        self.data_layer.store_feedback(feedback)
    
        # TODO Check the counter / scheduler
        train = False

        if train:
            self.ml_layer.ml_retrain(self.data_layer)
        
        return True
        
    def get_recommendations(userId, video_url):
        # TODO
        return None