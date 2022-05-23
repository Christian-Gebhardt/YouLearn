"""
Orchestrator to handle calls from endpoint (so they won't go directly to data layer or ml layer)
"""

import DataLayer
import HelperFunctions
import Params
    
def get_recommendations(userId, video_url):

    # 1. Get the features
    # 2. Call to mllayer
    # 3. Return the list
    
    return None
    
def feedback(user_id, video_url, feedback):
    
    # 1. Store the feedback to db?

    return None 