""" This file is used to make retweets about the AI """

from auth import *
from control import *

# Instantiate API:

api = auth_twitter_api()


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
