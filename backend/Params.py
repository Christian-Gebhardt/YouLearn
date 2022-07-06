"""
Static constants for the project
"""

import os

RUNNING_IN_CLOUD=os.environ.get("RUNNING_IN_CLOUD")

# Youtube
YT_API_KEY=os.environ.get("YT_API_KEY")
YT_REGION='DE'

# Database
DB_SERVER = os.getenv('MONGO_URI')
DB_LIMIT=100

# ML
PATH_TO_TRAINED_MODEL_MLP=os.environ.get("PATH_TO_TRAINED_MODEL_MLP")
NUM_OF_TRAINING_SAMPLES=1000