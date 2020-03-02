##IMPORTS
import string
import tweepy
import re
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

##SET UP TWITTER
consumer_key = "GuyAV6K3TnkMUHxRE0hmjOIaR"
consumer_secret = "PMp6HzVH8BK09VOnOwyon3SMH5NtDHJiGhr9A3HcpaZJB7IFXB"
access_token= "1566664404-SPzIXy4bazyMBc27kHu4XkiYwB0esCI5j3hLFVn"
access_token_secret = "cHfv3ntJPpyfAP0RLvfBeqCWprSMhcJwlzgAg1MnD1zf8"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
pos_emojis = '😙❤😍💓😗☺😊😛💕😀😃😚'
neg_emojis = '☹😕😩😒😠😐😦😣😫😖😞💔😢😟'
user = "realDonaldTrump"
user_tweets = api.user_timeline(screen_name = user ,count=200)

tweets = []
translator = str.maketrans('', '', string.punctuation)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
#        print('**',status.text.rstrip())
        tweets.append(status.text.rstrip())
        if len(tweets) > 200:
            myStream.disconnect()

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

all_emojis = list(pos_emojis + neg_emojis)
myStream.filter(track=all_emojis, languages=['en'])

def store_tweets(file, tweets):
    with open('tweets.txt', 'r') as f:
        all_tweets = f.readlines() + tweets

    tweets = list(set(all_tweets))
    
    with open('tweets.txt', 'w') as f:
        f.writelines([tweet.replace('\n','')+"\n" for tweet in tweets])
    return all_tweets


def clean_tweets(tweets):
    tweets = [tweet.rstrip() for tweet in tweets]
    tweets = [re.sub(r'\@\w+\b',"",tweet) for tweet in tweets]
    tweets = [re.sub(r'http\S+', '', tweet) for tweet in tweets]
    tweets = [tweet.translate(translator) for tweet in tweets]
    return tweets
    

def sort_tweets(tweets):
    positive_tweets = [tweet for tweet in tweets if set(tweet) & set(pos_emojis)]
    negative_tweets = [tweet for tweet in tweets if set(tweet) & set(neg_emojis)]
    positive_tweets = [re.sub(r'[^\x00-\x7F]+','', tweet) for tweet in positive_tweets]
    negative_tweets = [re.sub(r'[^\x00-\x7F]+','', tweet) for tweet in negative_tweets]
    return(positive_tweets, negative_tweets)


def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

def train_classifier(positive_tweets, negative_tweets):
    positive_tweets = [(create_word_features(word_tokenize(tweet)),'positive') for tweet in positive_tweets]
    negative_tweets = [(create_word_features(word_tokenize(tweet)),'negative') for tweet in negative_tweets]
    fraction_pos =  round(len(positive_tweets) * 0.8)
    fraction_neg =  round(len(negative_tweets) * 0.8)
    train_set = negative_tweets[:fraction_pos] + positive_tweets[:fraction_pos]
    test_set =  negative_tweets[fraction_neg:] + positive_tweets[fraction_neg:]
    classifier = NaiveBayesClassifier.train(train_set)
    accuracy = nltk.classify.util.accuracy(classifier, test_set)
    return classifier, accuracy


def calculate_naughty(classifier, accuracy, user_tweets):
    rating = [classifier.classify(create_word_features(word_tokenize(tweet))) for tweet in user_tweets]
    percent_naughty = rating.count('negative') / 200
    if percent_naughty > 0.5:
        print(user, "is", percent_naughty * 100, "percent NAUGHTY, with an accuracy of", accuracy)
    else:
        print(user, "is", 100 - (percent_naughty * 100), "percent NICE, with an accuracy of", accuracy)


tweets = store_tweets('tweets.txt', tweets)
tweets = clean_tweets(tweets)
user_tweets = [tweet.text for tweet in user_tweets]
user_tweets = clean_tweets(user_tweets)                                  
pos_tweets, neg_tweets = sort_tweets(tweets)
classifier, accuracy = train_classifier(pos_tweets, neg_tweets)
calculate_naughty(classifier, accuracy, user_tweets)
