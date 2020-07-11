""" The main file """

from interactions import *
from retweet import *

# Make Retweets:

make_rt(keywords=['#machinelearning', '#deeplearning', '#ai', '#artificialintelligence'],
        sleep=random.randint(60, 120))  # Sleep between 1 and 2 minutes 1280222600921321474

# Reply mentions and send thank u message:
reply(sleep=random.randint(60, 120))
