""" Make interactions such reply mentions and send messages """

import random
import time

from auth import *
from retweet import search_tweets

# Instantiate API:

api = auth_twitter_api()


# Stream to search just new mentions

class StreamListenerMentions(tweepy.StreamListener):
    def __init__(self, api_auth):
        super().__init__()
        self.api = api_auth
        self.me = api_auth.me()

    def on_status(self, tweet):
        print('Mention Found! ')
        print(f"{tweet.user.name}:{tweet.text}")
        reply(tweet, sleep=random.randint(60, 120))
        search_tweets(keywords=['#machinelearning', '#deeplearning', '#ai'])

    def on_error(self, status):
        print("Error detected")


# Reply tweets:

def reply(tweet, sleep):
    # Like the Mention:

    api.create_favorite(tweet.id)

    api.update_status(status='\N{yellow heart}', in_reply_to_status_id=tweet.id,
                      auto_populate_reply_metadata=True)

    api.send_direct_message(tweet.user.id, text='Hey, Thank you for mention me! \N{grinning face}')

    time.sleep(sleep)


# Search Mentions:

def search_mention(username):
    tweets_listener = StreamListenerMentions(api_auth=api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    mention = stream.filter(track=username)

    print(mention)

