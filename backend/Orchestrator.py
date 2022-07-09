"""
Orchestrator to handle calls from endpoint (so they won't go directly to data layer or ml layer)
"""

import DataLayer
import MlLayer
import Params
import threading

class Orchestrator():
    def __init__(self):
        self.ml_layer = MlLayer.MlLayer()
        self.data_layer = DataLayer.DataLayer()
        self.counter_until_retrain = 0
        self.retrain_thread = None
      
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

    def feedback(self, video_id, is_distractful):

        # 1. Store the feedback in the db collection feedback
        self.data_layer.store_feedback(video_id, is_distractful)
        self.counter_until_retrain+=1

        # 2. Check the counter if retraining is needed
        if self.counter_until_retrain >= Params.NUM_OF_FEEDBACKS_UNTIL_RETRAIN:
            print('retraining started')
            if self.retrain_thread is not None and self.retrain_thread.is_alive():
                print('Retraining already in progress!')
            else:
                self.retrain_thread = threading.Thread(target=self.ml_layer.ml_retrain, name="retrainer", args=[self.data_layer])
                self.retrain_thread.start()
                self.counter_until_retrain = 0

        return True

    def get_recommendations(userId, video_url):
        # TODO
        return None