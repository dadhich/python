import tweepy
from textblob import TextBlob

#Consumer API Keys
#API key = oRnek0LrVUCrbYIBNTXaXZM4V
#API secret key = zwbCrnodbBhK8Yv4BrPjOiZoui5r6ikU2Ld7hr9VASoEKmLSsP

#Access token & access token secret
#Access token = 147219444-bZi4MvFTyWsxAgIgYqpgTawXlSkSZb5ZkTtbvTjE
#Access token secret = EexG2ybTifuomUa2tarDMMqkF7C0ZQuCdVPAaaxwArx8G

consumer_key = 'oRnek0LrVUCrbYIBNTXaXZM4V'
consumer_secret = 'zwbCrnodbBhK8Yv4BrPjOiZoui5r6ikU2Ld7hr9VASoEKmLSsP'

access_token = '147219444-bZi4MvFTyWsxAgIgYqpgTawXlSkSZb5ZkTtbvTjE'
access_token_secret = 'EexG2ybTifuomUa2tarDMMqkF7C0ZQuCdVPAaaxwArx8G'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('dadhich')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)