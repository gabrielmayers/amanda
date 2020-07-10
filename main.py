import time

import tweepy


# Auth:

def auth_twitter(api_key, api_secret_key, access_tok, access_tok_secret):
    authentication = tweepy.OAuthHandler(api_key, api_secret_key)

    authentication.set_access_token(access_tok, access_tok_secret)

    return authentication


auth = auth_twitter('09nFtECOjaCCvL3JQjJcxvVLt', 'MplwsC879nCoFffxwXP1oWRRfD4l990ZK0o2tuE4mty9rXxS5N',
                    '1277383591014563840-ZoQ85Rlxh3MVsIrq8ljeDsNPtAy7jN',
                    'ct4YFqVn4bIaPvjSrv78GrtkP6BAivV0Nbz5kUcEIwQ1S')

api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)


def make_rt(keywords, sleep):
    search_results = api.search(q=[keywords], count=100)

    # Start API call counting incrementing 1:

    call = call_api(1)

    for results in search_results:

        try:
            api.retweet(id=results.id, count=1)

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


# Thank for mention:

def thank_u(id_user):
    api.send_direct_message(id_user, 'Thank u for mention me! S2')


# Reply tweets:

def reply(sleep):
    mentions = api.mentions_timeline()

    # Start API call counting incrementing 1:

    call = call_api(1)

    for results in mentions:

        try:
            api.update_status(status='\N{yellow heart}', in_reply_to_status_id=results.id,
                              auto_populate_reply_metadata=True)  # implement don't repeat comments

            # Increment 1 to the API call number:

            call = call + 1

            time.sleep(sleep)
        except:
            pass


reply(sleep=1)

# make_rt(keywords=['#machinelearning', '#deeplearning', '#ai', '#artificialintelligence'],
#       sleep=random.randint(60, 120))  # Sleep between 1 and 2 minutes 1280222600921321474
