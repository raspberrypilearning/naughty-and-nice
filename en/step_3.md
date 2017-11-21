## Setting up and testing your Twitter account

This step involves using a lot of code to fetch a user's Twitter stream and to fetch random live tweets.

- You will need a Twitter account and then will need to create a new App, associated with this account. An App is simply a program that you are linking to your Twitter account.  You can see how to do this in the collapsible section below.

[[[generic-api-registering-twitter]]]

- Now create a new Python file in your preferred editor (use IDLE if you have no preference) and call it `naughty_and_nice.py`.

- Into this file you can now set up your connection to Twitter, so that you can fetch a user's tweets and also fetch a live stream of current tweets. **Make sure to add in the path to your `twitter_auth.json` file correctly.**

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

- Next you need to create an empty list that will be used to store the live tweets, you will be reading from the Twitter stream.

```python
tweets = []
```

- For the last part of this section, you will create a `class` to read the twitter stream, limiting it to `200` tweets that will be stored in the list. Add this to the end of your file.

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

- Having written this, you can now test your code works. Add this line of code at the end of your file, to search Twitter for the word 'christmas'. This might take a long time to run.

```python
myStream.filter(track=["christmas"], languages=['en'])
```

- You can view the first tweet by typing `tweets[0]` in the shell, once the program has finished. Be warned though, that if you are using IDLE as your programming environment, it will crash if the tweet contains an emoji.
