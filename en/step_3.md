## Setting up and testing your Twitter account

This step involves using a lot of code to fetch random live tweets. You will need these as data for training your sentiment analysis program.

- Once you have a Twitter account, you will need to create a new app associated with this account. An app is simply a program that you link to your Twitter account. You can see how to do this in the collapsible section below.

[[[generic-api-registering-twitter]]]

- Now create a new Python 3 file in your preferred editor (use IDLE if you have no preference), and call it `naughty_and_nice.py`.

- In this file, set up your connection to Twitter, so that you can fetch a user's tweets and a live stream of current tweets. **Make sure to add in the path to your `twitter_auth.json` file correctly.**

```python
##IMPORTS
import tweepy
import json

##SET UP TWITTER
with open('/path/to/your/twitter_auth.json') as f:
    keys = json.load(f)
    
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
```

- Next you need to create an empty list to store the live tweets you will be reading from the Twitter stream.

```python
tweets = []
```

- For the last part of this section, you will create a `class` to read the twitter stream, limiting it to 200 tweets that will be stored in the `tweets` list. Add this code at the bottom of your file:

```python
##TWITTER STREAM
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        tweets.append(status.text.rstrip())
        if len(tweets) > 200:
            myStream.disconnect()

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
```

- Having written this, you can now test whether your code works by fetching live tweets. Add this line of code at the end of your file to search Twitter for the word 'christmas':

```python
myStream.filter(track=["christmas"], languages=['en'])
```

- Save and run your program — it might take a long time to run.

- Once the program has finished, you can view the first tweet you've stored by typing `tweets[0]` into the shell. Be warned though: if you are using IDLE as your programming environment, it will crash if the tweet contains an emoji.
