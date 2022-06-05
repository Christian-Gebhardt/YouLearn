"""
Machine learning layer
"""

import DataLayer
import numpy as np
import pandas as pd
import json

def ml_filter_distractful(df):
    # Returns df with distractful videos
    model = DataLayer.get_trained_model()
    predicted = model.predict(df['to_predict'].tolist())

    df_distractful = df[np.invert(np.array(predicted, dtype=bool))]

    return json.dumps({'distractful_ids' : df_distractful['video_id'].to_list()})