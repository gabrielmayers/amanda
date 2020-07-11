""" This file is used for make authentication in the Twitter API """

import tweepy


# Auth:

def auth_data(api_key, api_secret_key, access_tok, access_tok_secret):
    authentication = tweepy.OAuthHandler(api_key, api_secret_key)

    authentication.set_access_token(access_tok, access_tok_secret)

    return authentication


def auth_twitter_api():
    auth = auth_data('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                     'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                     'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

    api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

    return api
