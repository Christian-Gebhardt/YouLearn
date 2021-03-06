import Params
from pymongo import MongoClient
from apiclient.discovery import build

def get_yt_client():
    return build('youtube', 'v3', developerKey=Params.YT_API_KEY) 

def get_db():
    mongo_client = MongoClient(Params.DB_SERVER)
    return mongo_client['youtube-db']