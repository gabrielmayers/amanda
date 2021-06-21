""" Make retweets about the Machine Learning, AI and Deep Learning hashtags """

import random
import time

from auth import *
from interactions import *

# Instantiate API:

api = auth_twitter_api()


# Stream to search just new mentions

class StreamListenerTweets(tweepy.StreamListener):

    post_counter = 0

    def __init__(self, api_auth):
        super().__init__()
        self.api = api_auth
        self.me = api_auth.me()

    def on_status(self, tweet):
        print('Tweet Found!')
        print(f"{tweet.user.name} {tweet.text}")

        try:
          make_rt(tweet)
          print("Twitted!")
         
          print("\n ==================================================== \n Sleeping... \n")

          time.sleep(random.randint(5, 60))
        except:
            print("An Error ocurred when tried to make retweet!")
            print(f"{tweet.user.name} {tweet.text}")
            pass

    def on_error(self, status):
        print("Error detected")


# Search Mentions:

def search_tweets(keywords):
    tweets_listener = StreamListenerTweets(api_auth=api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords)


def make_rt(tweet):
    # Make Retweet:

    try:
        api.create_favorite(tweet.id)
    except:
        pass

    api.retweet(tweet.id)
