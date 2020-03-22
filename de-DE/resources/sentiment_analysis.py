import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

negative_tweets = twitter_samples.strings('negative_tweets.json')
positive_tweets = twitter_samples.strings('positive_tweets.json')

negative_tweets = [string.replace(":", "").replace(")", "").replace("(", "") for string in negative_tweets]
positive_tweets = [string.replace(":", "").replace(")", "").replace("(", "") for string in positive_tweets]

pos_tweets = []
neg_tweets = []

for tweet in positive_tweets:
    pos_tweets.append((create_word_features(word_tokenize(tweet)), "positive"))
for tweet in negative_tweets:
    neg_tweets.append((create_word_features(word_tokenize(tweet)), "negative"))

tweet = "The state of Virginia economy, under Democrat rule, has been terrible. If you vote Ed Gillespie tomorrow, it will come roaring back!"

train_set = neg_tweets + pos_tweets



classifier = NaiveBayesClassifier.train(train_set)
accuracy = nltk.classify.util.accuracy(classifier, test_set)

words = word_tokenize(tweet)
words = create_word_features(words)
print(classifier.classify(words))
