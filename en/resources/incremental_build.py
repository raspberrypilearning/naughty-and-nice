##IMPORTS
import tweepy
import json
import re
import string

##SET UP TWITTER
with open('/home/mjs/twitter_auth.json') as f:
    keys = json.load(f)
    
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = []

##TWITTER STREAM
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
#        print('**',status.text.rstrip())
        tweets.append(status.text.rstrip())
        if len(tweets) > 200:
            myStream.disconnect()

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

##EMOJI DATA
pos_emojis = '😙❤😍💓😗☺😊😛💕😀😃😚'
neg_emojis = '☹😕😩😒😠😐😦😣😫😖😞💔😢😟'
all_emojis = list(pos_emojis + neg_emojis)

##FETCH SOME TWEETS

myStream.filter(track=all_emojis, languages=['en'])

def store_tweets(file, tweets):
    with open('tweets.txt', 'r') as f:
        old_tweets = f.readlines()

    all_tweets = tweets + old_tweets
    all_tweets = list(set(all_tweets))
    all_tweets = [tweet.replace('\n','')+"\n" for tweet in all_tweets]

    with open('tweets.txt', 'w') as f:
        f.writelines(all_tweets)

    return all_tweets

def clean_tweets(tweets):
    tweets = [tweet.rstrip() for tweet in tweets]
    tweets = [re.sub(r'@\S+', '', tweet) for tweet in tweets]
    tweets = [re.sub(r'http\S+', '', tweet) for tweet in tweets]
    tweets = [tweet.translate({ord(char): '' for char in string.punctuation}) for tweet in tweets]
    return tweets

##EXECUTE THE PROGRAM
tweets = store_tweets('tweets.txt', tweets)
tweets = clean_tweets(tweets)
