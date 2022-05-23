"""
Generic helper functions for the project
"""

import Params
import ast
from apiclient.discovery import build
from urllib import parse

client = build('youtube', 'v3', developerKey=Params.YT_API_KEY)

def extract_features(video_url):
    video_id = get_video_id_from_url(video_url)
    data = client.videos().list(id=video_id, part="snippet").execute()
   
    snippet = data['items'][0]['snippet'] 
    title = snippet['title']
    description = snippet['description']
    tags = snippet['tags']
    category = get_category_name_from_id(snippet['categoryId'])

    return title, description, tags, category

def get_video_id_from_url(video_url):
    url_parsed = parse.urlparse(video_url)
    qsl = parse.parse_qs(url_parsed.query)
    return qsl['v'][0]

def get_category_name_from_id(video_category_id):
    data = client.videoCategories().list(part='snippet', regionCode=Params.YT_REGION).execute()

    categories = data['items']

    for category in categories: 
        if category['id'] == video_category_id: return category['snippet']['title']

title, description,tags, categories = extract_features("https://www.youtube.com/watch?v=Oq-frA8uYeU")

for x in (title, description, tags, categories,):
    print(x, "\n")
