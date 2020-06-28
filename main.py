import tweepy

# Authenticate to Twitter

auth = tweepy.OAuthHandler("6vb95s6RCO5VS3WbI9VtD8KA0", "BsbMbrjnThkQhd2W14tZuTTFqUyO5F10bTJOS9AFb8aFu4F5A2")

auth.set_access_token("1262531460894011395-Xd9xt4PacAbowV7JOp1qrzhC6EKJbM", "5nb9Z1qMuS4qrlYzm1QwE8xOflhs9sOAQtK4O42QKTqSe")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Ok!")

except:
    print("Error During Authentication")
