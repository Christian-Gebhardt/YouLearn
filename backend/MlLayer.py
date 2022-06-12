"""
Machine learning layer
"""

import numpy as np
import pandas as pd
import json

def ml_filter_distractful(model, df):
    # Returns df with distractful videos
    predicted = model.predict(df['to_predict'].tolist())

    df_distractful = df[np.invert(np.array(predicted, dtype=bool))]

    return json.dumps({'distractful_ids' : df_distractful['video_id'].to_list()})