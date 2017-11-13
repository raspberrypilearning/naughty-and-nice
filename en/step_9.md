## Training a classifier

The `classifier` will be able to tell if a tweet has a positive or negative sentiment. First it needs training though, to teach it what positive tweets and negative tweets look like.

- A few new module will need to be imported at the top of you program

```python
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
```

- Start by creating a new function called `train_classifier`. It needs the positive and negative tweets as parameters.

```python
def train_classifier(positive_tweets, negative_tweets):
```

- The next thing to do is to create new data structures that will like the words in the positive tweets to having a positive sentiment and the words in the negative tweet as having a negative sentiment. This simply creates tuples of tweets, containing the dictionary created in the `parse_tweets` function and then the word `positive` or `negative` depending on which list the tweet came from.

```python
def train_classifier(positive_tweets, negative_tweets):
    positive_tweets = [(parse_tweets(tweet),'positive') for tweet in positive_tweets]
    negative_tweets = [(parse_tweets(tweet),'negative') for tweet in negative_tweets]
```

- Now you don't want to use all the tweets to train the classifier. Some tweets should be kept back so they can be used to calculate how accurate the classifier is. So only 80% of the tweets will be used in training.

```python
def train_classifier(positive_tweets, negative_tweets):
    positive_tweets = [(parse_tweets(tweet),'positive') for tweet in positive_tweets]
    negative_tweets = [(parse_tweets(tweet),'negative') for tweet in negative_tweets]
	fraction_pos =  round(len(positive_tweets) * 0.8)
    fraction_neg =  round(len(negative_tweets) * 0.8)
```

- Next the training se and the testing set can be created, by joining 80% of the positive tweets and 80% of the negative tweets into one giant list of categorised tweets. The remianing tweets are used in the testing set. Then the `classifier` can be created and the accuracy calculated.

```python
def train_classifier(positive_tweets, negative_tweets):
    positive_tweets = [(parse_tweets(tweet),'positive') for tweet in positive_tweets]
    negative_tweets = [(parse_tweets(tweet),'negative') for tweet in negative_tweets]
	fraction_pos =  round(len(positive_tweets) * 0.8)
    fraction_neg =  round(len(negative_tweets) * 0.8)
	
    train_set = negative_tweets[:fraction_pos] + positive_tweets[:fraction_pos]
    test_set =  negative_tweets[fraction_neg:] + positive_tweets[fraction_neg:]
    classifier = NaiveBayesClassifier.train(train_set)
    accuracy = nltk.classify.util.accuracy(classifier, test_set)
    return classifier, accuracy
```
- Then call the function on the last line of your program

```python
classifier, accuracy = train_classifier(pos_tweets, neg_tweets)
```

- Have a look at the video below if you want to learn a little more about the classifier and the accuracy.

<video width="560" height="315" controls>
<source src="images/vid_11.webm" type="video/webm">
Your browser does not support WebM video, try FireFox or Chrome
</video>
