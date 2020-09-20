""" Make retweets about the Machine Learning, AI and DeepLearning hashtags """

import random
import time

from auth import *
from interactions import *

# Instantiate API:

api = auth_twitter_api()


# Stream to search just new mentions

class StreamListenerTweets(tweepy.StreamListener):
    def __init__(self, api_auth):
        super().__init__()
        self.api = api_auth
        self.me = api_auth.me()

    def on_status(self, tweet):
        print('Tweet Found! ')
        print(f"{tweet.user.name}:{tweet.text}")
        make_rt(tweet, sleep=random.randint(60, 120))

    def on_error(self, status):
        print("Error detected")


# Search Mentions:

def search_tweets(keywords):
    tweets_listener = StreamListenerTweets(api_auth=api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords)


def make_rt(tweet, sleep):
    # Make Retweet:

    api.create_favorite(tweet.id)

    api.retweet(tweet.id)

    time.sleep(sleep)
