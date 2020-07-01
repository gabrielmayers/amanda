import time

import tweepy


# Auth:

def auth_twitter(api_key, api_secret_key, access_tok, access_tok_secret):
    authentication = tweepy.OAuthHandler(api_key, api_secret_key)

    authentication.set_access_token(access_tok, access_tok_secret)

    return authentication


auth = auth_twitter('09nFtECOjaCCvL3JQjJcxvVLt', 'MplwsC879nCoFffxwXP1oWRRfD4l990ZK0o2tuE4mty9rXxS5N',
                    '1277383591014563840-C2xq6pPHS28H3yNiqP4lH1VnUOurMe',
                    'Lhl6vSliXdadfLhxWG2jDjcAkA9UmoQPPbA0XU05YZHFH')

api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)


def make_rt(keywords, sleep):
    for i in api.search(q=[keywords]):

        try:
            api.retweet(i.id)

        except:
            pass

    time.sleep(sleep)


make_rt(['#machinelearning', '#deeplearning', '#ai', '#artificialintelligence'], 60)
