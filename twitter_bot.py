import tweepy

print('My twitter bot')

CONSUMER_KEY = 'Ynp4mUtKAnPInBEArOIZOkrpB'
CONSUMER_SECRET = '9QtuapLtfPwqAhcx2Vw5xFiZL2DzYD9lhorxhRAvwMZZUR8dJ'
ACCESS_KEY = '1661771091797323791-HOY5uaAKvkq3zcJTlcKIIRayGbM4dC'
ACCESS_SECRET = '0lnvpq7eIHYdAah5AP0YsXePPoYWbireWOmcpX2EW3rh3'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
