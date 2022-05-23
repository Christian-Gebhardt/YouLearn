"""
Database helper
"""

import Params
from pymongo import MongoClient

def connect_db():
    client = MongoClient(Params.DB_SERVER)
    return client

# TODO