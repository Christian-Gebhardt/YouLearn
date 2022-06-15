"""
Machine learning layer
"""

import numpy as np
import pandas as pd
import json
import sklearn

def ml_filter_distractful(model, df):
    # Returns df with distractful videos
    predicted = model.predict(df['to_predict'].tolist())

    df_distractful = df[np.invert(np.array(predicted, dtype=bool))]

    return json.dumps({'distractful_ids' : df_distractful['video_id'].to_list()})

def ml_filter_and_sort_distractful(model, df):
    # Returns df with distractful videos
    predicted = model.predict_proba(df['to_predict'].tolist()) 
    probabilities = pd.DataFrame(predicted[:,1], columns=['probability_of_educational'])

    # DF - videos with probabilities
    df = pd.concat([df, probabilities], axis=1)
    df = df[df['probability_of_educational'] > 0.5]
    df = df.sort_values('probability_of_educational', ascending=False)
    
    print(df['video_id'].to_list())

    return json.dumps({'recommended_and_sorted_ids' : df['video_id'].to_list()})