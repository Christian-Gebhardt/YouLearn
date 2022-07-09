"""
Machine learning layer
"""

import Params
import pickle
import numpy as np
import pandas as pd
import json
import sklearn
import DataLayer

class MlLayer:
    def __init__(self):
        self.model = DataLayer.DataLayer().load_trained_model()

    def ml_filter_distractful(self, df):
        # Returns df with distractful videos
        predicted = self.model.predict(df['to_predict'].tolist())

        df_distractful = df[np.invert(np.array(predicted, dtype=bool))]

        return json.dumps({'distractful_ids' : df_distractful['video_id'].to_list()})

    def ml_filter_and_sort_distractful(self, filter_threshold, df):
        # Returns df with distractful videos
        predicted = self.model.predict_proba(df['to_predict'].tolist()) 
        probabilities = pd.DataFrame(predicted[:,1], columns=['probability_of_educational'])

        # DF - videos with probabilities
        df = pd.concat([df, probabilities], axis=1)
        df = df[df['probability_of_educational'] > filter_threshold]
        print('using threshold:', filter_threshold)
        df = df.sort_values('probability_of_educational', ascending=False)
        
        return json.dumps({'recommended_and_sorted_ids' : df['video_id'].to_list()})

    def ml_retrain(self, data_layer):
        # Method that retrains the model and calls datalayer to store it

        if len(data_layer.dataset_feedbacks) < Params.NUM_OF_TRAINING_SAMPLES:
            num_from_kaggle = Params.NUM_OF_TRAINING_SAMPLES - len(data_layer.dataset_feedbacks)
            random_train = data_layer.dataset_kaggle.sample(n=num_from_kaggle)
            df = pd.concat([random_train, data_layer.dataset_feedbacks])
        else:
            df = data_layer.dataset_feedbacks.sample(n=Params.NUM_OF_TRAINING_SAMPLES)
    
        x_train = df['title'] + " " + df['description']
        y_train = df['category_id']

        # Warmstart by default
        self.model['clf'].n_iter_ = 0
        self.model['clf'].best_loss_ = 1
        self.model.fit(x_train, y_train)

        # Save the model to file using pickle
        data_layer.store_model(self.model)
