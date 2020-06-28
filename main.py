import tweepy

# Authenticate to Twitter

auth = tweepy.OAuthHandler("XXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

auth.set_access_token("XXXXXXXXXXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

api.update_status("Testing Tweet!")
