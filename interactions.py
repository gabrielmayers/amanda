""" Make interactions such reply mentions and send messages """

import random

from auth import *
from control import *

# Instantiate API:

api = auth_twitter_api()


# Thank for mention:

def thank_u(user, call_score):
    api.send_direct_message(user, text='Hey, Thank you for mention me! \N{grinning face}')

    call_score = call_score + 1

    return call_score


# Reply tweets:

def reply(sleep):
    mentions = api.mentions_timeline()

    # Start API call counting incrementing 1:

    call = call_api(1)

    for results in mentions:

        try:
            call_update_count = api.update_status(status='\N{yellow heart}', in_reply_to_status_id=results.id,
                                                  auto_populate_reply_metadata=True)  # implement don't repeat comments

            call_send_count = thank_u(results.user.id, call_score=call)  # Send Message to say Thank U

            # TODO Verify if i'm already replied this mention

            # Increment update and send api call(1 and 1):

            call = call + call_update_count + call_send_count

            time.sleep(sleep)
        except:
            pass

    reply(sleep=random.randint(60, 120))  # Search for Mentions Again
