""" Make retweets about the Machine Learning, AI and DeepLearning hashtags """

import random

from auth import *
from control import *
from interactions import favorite


# Stream to search just new mentions

class StreamListenerTweets(tweepy.StreamListener):
    def __init__(self, api_auth):
        super().__init__()
        self.api = api_auth
        self.me = api_auth.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")
        make_rt(tweet, sleep=random.randint(60, 120))

    def on_error(self, status):
        print("Error detected")


# Instantiate API:

api = auth_twitter_api()


# Search Mentions:

def search_tweets(keywords):
    tweets_listener = StreamListenerTweets(api_auth=api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords)


def make_rt(tweet, sleep):
    # Make Retweet:

    favorite(tweet.id, 1)

    api.retweet(tweet.id)

    time.sleep(sleep)
