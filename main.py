import tweepy

# Authenticate to Twitter

auth = tweepy.OAuthHandler("XXXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXX")

auth.set_access_token("XXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXX")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Ok!")

except:
    print("Error During Authentication")
