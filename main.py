import time

import tweepy


# Auth:

def auth_twitter(api_key, api_secret_key, access_tok, access_tok_secret):
    authentication = tweepy.OAuthHandler(api_key, api_secret_key)

    authentication.set_access_token(access_tok, access_tok_secret)

    return authentication


auth = auth_twitter('XXXXXXXXXXXXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXXXXXXXXX',
                    'XXXXXXXXXXXXXXXXXXXXXXXXXXX',
                    'XXXXXXXXXXXXXXXXXXXXXXXXXXX')

api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)


def make_rt(keywords, sleep):
    for i in api.search(q=[keywords]):

        try:
            api.retweet(i.id)

        except:
            pass

    time.sleep(sleep)


make_rt(['#machinelearning', '#deeplearning', '#ai', '#artificialintelligence'], 300)
