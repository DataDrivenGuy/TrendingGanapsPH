import os
import tweepy


def tw_oauth():
    # consumer_key = config('consumerKey')
    # consumer_secret = config('consumerSecret')
    # access_token = config('accessToken')
    # access_token_secret = config('accessTokenSecret')

    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)