""" Make interactions such reply mentions and send messages """

import random

from auth import *
from control import *


# Stream to search just new mentions

class StreamListenerMentions(tweepy.StreamListener):
    def __init__(self, api_auth):
        super().__init__()
        self.api = api_auth
        self.me = api_auth.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")
        reply(tweet, sleep=random.randint(60, 120))

    def on_error(self, status):
        print("Error detected")


# Instantiate API:

api = auth_twitter_api()


# Thank for mention:

def thank_u(user, call_score):
    api.send_direct_message(user, text='Hey, Thank you for mention me! \N{grinning face}')

    call_score = call_score + 1

    return call_score


# Like

def favorite(tweet_id):
    api.create_favorite(tweet_id)


# Reply tweets:

def reply(tweet, sleep):
    # Like the Mention:

    favorite(tweet.id, 1)

    api.update_status(status='\N{yellow heart}', in_reply_to_status_id=tweet.id,
                      auto_populate_reply_metadata=True)

    thank_u(tweet.user.id, 1)

    time.sleep(sleep)


# Search Mentions:

def search_mention():
    tweets_listener = StreamListenerMentions(api_auth=api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=['@amandamlbot'])
