##IMPORTS
import tweepy
import json
import re
import string
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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
user = "coding2learn"
user_tweets = api.user_timeline(screen_name = user ,count=200)

def store_tweets(file, tweets):
    '''Read tweets from file and write new tweets to the file'''
    with open('tweets.txt', 'r') as f:
        old_tweets = f.readlines()
    
    all_tweets = old_tweets + tweets
    all_tweets = list(set(all_tweets))
    all_tweets = [tweet.replace('\n','')+"\n" for tweet in all_tweets]
    
    with open('tweets.txt', 'w') as f:
        f.writelines(all_tweets)

    return all_tweets


def clean_tweets(tweets):
    '''Remove new lines and puntuation from tweets'''
    translator = str.maketrans('', '', string.punctuation)    
    tweets = [tweet.rstrip() for tweet in tweets]
    tweets = [re.sub(r'\@\w+\b',"",tweet) for tweet in tweets]
    tweets = [re.sub(r'http\S+', '', tweet) for tweet in tweets]
    tweets = [tweet.translate(translator) for tweet in tweets]
    return tweets
    

def sort_tweets(tweets):
    '''Sort tweets based on emojis'''
    positive_tweets = [tweet for tweet in tweets if set(tweet) & set(pos_emojis)]
    negative_tweets = [tweet for tweet in tweets if set(tweet) & set(neg_emojis)]
    positive_tweets = [re.sub(r'[^\x00-\x7F]+','', tweet) for tweet in positive_tweets]
    negative_tweets = [re.sub(r'[^\x00-\x7F]+','', tweet) for tweet in negative_tweets]
    return(positive_tweets, negative_tweets)


def categorise_tweets(words):
    '''Turn tweets into form understood by sentiment anlysis tool'''
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

def train_classifier(positive_tweets, negative_tweets):
    '''Train the sentiment analysis'''
    positive_tweets = [(categorise_tweets(word_tokenize(tweet)),'positive') for tweet in positive_tweets]
    negative_tweets = [(categorise_tweets(word_tokenize(tweet)),'negative') for tweet in negative_tweets]
    fraction_pos =  round(len(positive_tweets) * 0.8)
    fraction_neg =  round(len(negative_tweets) * 0.8)
    train_set = negative_tweets[:fraction_pos] + positive_tweets[:fraction_pos]
    test_set =  negative_tweets[fraction_neg:] + positive_tweets[fraction_neg:]
    classifier = NaiveBayesClassifier.train(train_set)
    accuracy = nltk.classify.util.accuracy(classifier, test_set)
    return classifier, accuracy


def calculate_naughty(classifier, accuracy, user_tweets):
    '''Run sentiment analysis'''
    rating = [classifier.classify(categorise_tweets(word_tokenize(tweet))) for tweet in user_tweets]
    percent_naughty = rating.count('negative') / 200
    if percent_naughty > 0.5:
        print(user, "is", percent_naughty * 100, "percent NAUGHTY, with an accuracy of", accuracy)
    else:
        print(user, "is", 100 - (percent_naughty * 100), "percent NICE, with an accuracy of", accuracy)

##EXECUTE
tweets = store_tweets('tweets.txt', tweets)
tweets = clean_tweets(tweets)
user_tweets = [tweet.text for tweet in user_tweets]
user_tweets = clean_tweets(user_tweets)                                  
pos_tweets, neg_tweets = sort_tweets(tweets)
classifier, accuracy = train_classifier(pos_tweets, neg_tweets)
calculate_naughty(classifier, accuracy, user_tweets)
