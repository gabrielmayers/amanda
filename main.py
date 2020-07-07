import random
import time

import tweepy


# Auth:

def auth_twitter(api_key, api_secret_key, access_tok, access_tok_secret):
    authentication = tweepy.OAuthHandler(api_key, api_secret_key)

    authentication.set_access_token(access_tok, access_tok_secret)

    return authentication


auth = auth_twitter('09nFtECOjaCCvL3JQjJcxvVLt', 'MplwsC879nCoFffxwXP1oWRRfD4l990ZK0o2tuE4mty9rXxS5N',
                    '1277383591014563840-Q5bZURznGNks7KfbqPcGrZtISAnT5c',
                    'Dxba7K9Cft9NM1LifoOJit87gflaBsfWT7KE5p7nu7nIY')

api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)


def make_rt(keywords, sleep):
    search_results = api.search(q=[keywords], count=100)

    # Start API call counting incrementing 1:

    call = call_api(1)

    for i in search_results:

        try:
            api.retweet(id=i.id, count=1)

            # Increment 1 to the API call number:

            call = call + 1

            time.sleep(sleep)
        except:
            pass

    verify_call(call)


# Function to count each API call and prevent spam:

def call_api(call):
    call = call + 1
    return call


# Verify number of call and prevent spam:

def verify_call(call):
    if call > 50:
        time.sleep(900)
    else:
        pass


make_rt(keywords=['#machinelearning', '#deeplearning', '#ai', '#artificialintelligence'],
        sleep=random.randint(60, 120))  # Sleep between 1 and 2 minutes
