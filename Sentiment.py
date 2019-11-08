import tweepy
from textblob import TextBlob

#our login info to access the twitter api
consumer_key = 'a3q4whtJGT9mK5mEZ5GDFi6OE'
consumer_secret = 'JV1q33bV4Qmy8NQ3WNg9sVwBoBCkQEsol6uw98rTsCU0ZcWSCz'

access_token = '1190385893531504640-svLYTYHd5HRDiR9IrSbBajHJdlzTd6'
access_token_secret = 'dtYnrybqugOVixxa0hqBvBuITHRDsbeFjslf8DqD8PWgL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#creating an API variable can allow us to create, delete, or search for tweets
api = tweepy.API(auth)

#here we use the twitter api to look for any tweets with a given Keyword
#in our case our keyword is CSUN
public_tweets = api.search('CSUN')

#for loop that goes through a number of tweets that gathers and prints them
for tweet in public_tweets:
	#getting the raw text from the tweet and printing to the console
	print(tweet.text)
	#the sentiment anlaysis is performed and stored in the analysis variable
	#this gives us the polarity (positive or negative) and subjectivity (object or subjective) values
	analysis = TextBlob(tweet.text)
	#sentiment analysis values are printed along with the given tweet
	print(analysis.sentiment)
	
