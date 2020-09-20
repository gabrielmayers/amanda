""" Make authentication in the Twitter API """

import tweepy


# Auth:

def auth_data(api_key, api_secret_key, access_tok, access_tok_secret):
    authentication = tweepy.OAuthHandler(api_key, api_secret_key)

    authentication.set_access_token(access_tok, access_tok_secret)

    return authentication


def auth_twitter_api():
    auth = auth_data('dQ5TRIQSvGxBSK9yhp5uZasH0', 'WCgYefgrudtOcoG2N5lBRjMgl4xSbmjgwuqSQCzia091M61ijW',
                     '1277383591014563840-ebTl4qEg38DbFEKdqwnKrHMIEhxw9e',
                     'YbxSajXEKlS82GeD23ZkNFsxo99LEqCobkF8iC0YnHLW7')

    api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

    return api
