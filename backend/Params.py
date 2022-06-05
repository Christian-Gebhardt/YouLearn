"""
Static constants for the project
"""

import os

# Youtube
YT_API_KEY=os.environ.get("YT_API_KEY")
YT_REGION='DE'

# Database
DB_SERVER = ''
PORT = 0
USER_NAME = ''
PASSWORD = ''
DB_NAME = ''

# ML
PATH_TO_TRAINED_MODEL_MLP=os.environ.get("PATH_TO_TRAINED_MODEL_MLP")