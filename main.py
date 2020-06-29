import tweepy

# Authenticate to Twitter

auth = tweepy.OAuthHandler("09nFtECOjaCCvL3JQjJcxvVLt", "MplwsC879nCoFffxwXP1oWRRfD4l990ZK0o2tuE4mty9rXxS5N")

auth.set_access_token("1277383591014563840-ZJNhopLOEajbdwq0k8wc6fmqSyST1Y", "cGsbRZzZOB0lM6AY24774DaxBlrTgVA6KSakp1qmr8EWn")

api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

for i in api.search(q='#machinelearning', count=2):
    api.retweet(i.id)
