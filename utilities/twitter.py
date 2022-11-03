import os
import tweepy

def tw_oauth():
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
    bearer_token = os.environ['BEARER_TOKEN']

    client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token,
                           access_token_secret=access_token_secret)

    return client