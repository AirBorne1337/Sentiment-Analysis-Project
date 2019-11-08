import tweepy
from textblob import TextBlob

consumer_key = 'a3q4whtJGT9mK5mEZ5GDFi6OE'
consumer_secret = 'JV1q33bV4Qmy8NQ3WNg9sVwBoBCkQEsol6uw98rTsCU0ZcWSCz'

access_token = '1190385893531504640-svLYTYHd5HRDiR9IrSbBajHJdlzTd6'
access_token_secret = 'dtYnrybqugOVixxa0hqBvBuITHRDsbeFjslf8DqD8PWgL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#creating an API variable can allow us to create, delete, search for tweets
api = tweepy.API(auth)

public_tweets = api.search('CSUN')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	
