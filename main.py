import tweepy

# Authenticate to Twitter

auth = tweepy.OAuthHandler("09nFtECOjaCCvL3JQjJcxvVLt", "MplwsC879nCoFffxwXP1oWRRfD4l990ZK0o2tuE4mty9rXxS5N")

auth.set_access_token("1277383591014563840-tYygJDOMyAC5b2guuMCafhvg6Scq4B", "o3RyHAj26esFqbvDypsbS0Qu24dTmcbODYaQpRKdO7HxW")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

api.update_status("Testing tweet from Tweepy")