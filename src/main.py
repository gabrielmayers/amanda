""" The main file """

from interactions import *
from retweet import *

# Make Retweets:

# search_tweets(keywords=['#machinelearning', '#deeplearning', '#ai'])

# Reply mentions and send thank u message:

since_id = 1

while True:
    since_id = check_mentions(["@AmieAndYou"], since_id)
    print("Waiting...")
    time.sleep(60)
