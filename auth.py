""" Make authentication in the Twitter API """

import tweepy


# Auth:

def auth_data(api_key, api_secret_key, access_tok, access_tok_secret):
    authentication = tweepy.OAuthHandler(api_key, api_secret_key)

    authentication.set_access_token(access_tok, access_tok_secret)

    return authentication


def auth_twitter_api():
    auth = auth_data('G2crPtsjdGoAxGpCwY3fwWxmF', 'dbdH35od0z5oEqzdEUM6T3jOJH4yMi6aqHkShSeqoMBAQiR0pg',
                     '1277383591014563840-8w66TNjyRrIe7OukkUtR8WPTgYYN9O',
                     'oXobs5IiBwR9VODjLJ0Em1Tck5kKluOLowlni2EsnQrjw')

    api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

    return api
