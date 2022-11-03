import streamlit as st
import pandas as pd
import tweepy
import os
import json
import sys
import geocoder
import requests
import os
import json
import pickle

from dotenv import load_dotenv

load_dotenv()
bearer_token = os.environ['BEARER_TOKEN']

client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)
query = 'pasend'

tweets = tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=[
                          'context_annotations', 'created_at'], max_results=100).flatten(limit=10000)

# Convert the search results into a pandas dataframe
df = pd.DataFrame(tweets)
# Print first five the tweet ids and tweets
df[['id', 'text']].head()

with open('pasend.pickle', 'wb') as handle:
    pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)

# with open('pasend.pickle', 'rb') as handle:
#     df = pickle.load(handle)
#
# pd.set_option('display.width', 1000)
# pd.set_option('display.max_columns', 1000)
# print(df)

