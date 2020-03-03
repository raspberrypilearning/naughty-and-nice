## Training a classifier

We will now create a **`classifier`** that will be able to tell if a tweet has a positive or negative sentiment. First we need to train it though, to teach it what positive tweets and negative tweets look like. To do the training, we will use the dataset of random tweets we have fetched.

If you're not interested in how the `classifier` works, as it might be a bit tricky to understand, then the full code for the function is provided at the bottom of this step. 

- Two new modules will need to be imported at the top of your program:

```python
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
```

- Then create a new function called `train_classifier`, which takes the positive and negative tweets as parameters.

```python
def train_classifier(positive_tweets, negative_tweets):
```

The first thing to do in the function is to create a new data structure that will take the words in the positive tweets and assign them a positive sentiment, and another data structure that will take the words in the negative tweet and assign them a negative sentiment. This simply creates tuples, in which each dictionary created by the `parse_tweets` function is followed by the word `positive` or `negative`, depending on which list the original tweet came from. So for a single tweet, you might get a tuple that looks like this:

```python
({'why': True, 'want': True, 'talk': True, 'happy': True, 'today': True, 'hello': True}, 'positive')
```

- Add these lines to your function to create the tuples:

```python
def train_classifier(positive_tweets, negative_tweets):
    positive_tweets = [(parse_tweets(tweet),'positive') for tweet in positive_tweets]
    negative_tweets = [(parse_tweets(tweet),'negative') for tweet in negative_tweets]
```

You don't want to use all the tweets to train the `classifier` — some tweets should be kept back so that you can use them later to calculate how accurate the `classifier` is. Therefore, only 80% of the tweets will be used in training.

- Add two lines of code to your function to determine which fractions of your tweets you will use for training:

```python
def train_classifier(positive_tweets, negative_tweets):
	positive_tweets = [(parse_tweets(tweet),'positive') for tweet in positive_tweets]
	negative_tweets = [(parse_tweets(tweet),'negative') for tweet in negative_tweets]
	fraction_pos =  round(len(positive_tweets) * 0.8)
	fraction_neg =  round(len(negative_tweets) * 0.8)
```

- Next, the training set can be created by joining 80% of the positive tweets and 80% of the negative tweets into one giant list of categorised tweets. The remaining tweets are used in the testing set. Then the `classifier` can be created and the accuracy calculated.

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

- Now call the function on the last line of your program:

```python
classifier, accuracy = train_classifier(pos_tweets, neg_tweets)
```

- Have a look at the video below if you want to learn a little more about the classifier and its accuracy.

<video width="560" height="315" controls>
<source src="images/vid_11.webm" type="video/webm">
Your browser does not support WebM video, so try FireFox or Chrome.
</video>
