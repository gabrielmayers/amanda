""" This file is used for make authentication in the Twitter API """

import tweepy


# Auth:

def auth_data(api_key, api_secret_key, access_tok, access_tok_secret):
    authentication = tweepy.OAuthHandler(api_key, api_secret_key)

    authentication.set_access_token(access_tok, access_tok_secret)

    return authentication


def auth_twitter_api():
    auth = auth_data('09nFtECOjaCCvL3JQjJcxvVLt', 'MplwsC879nCoFffxwXP1oWRRfD4l990ZK0o2tuE4mty9rXxS5N',
                     '1277383591014563840-BFfIpgpJtUIHtNJiLRH374BSm8bXqt',
                     'tnrnRmXn0NaCWyrGWrlEQ5lbT7XDRGyHzjzq02jiDQsom')

    api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

    return api
