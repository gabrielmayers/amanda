""" This class is used to prevent SPAM controlling the number of interactions and API calls """

import time


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
