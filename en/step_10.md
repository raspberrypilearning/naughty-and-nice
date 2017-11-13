## Calculating naughtiness

Now that you can tell if a tweet is positive or negative, you can fetch a user's last two hundred tweets and see if they mostly talk about negative or positive things. This will help you know if they're naughty or nice.

- Start by creating a new function and call it `calculate_naughty`. It should have the classifier, accuracy and a twitter username is parameters.

```python
def calculate_naughty(classifier, accuracy, user):
```

- Next you can fetch the last 200 tweets of any twitter user. The list of tweets will also need to be cleaned, using the `clean_tweets` function.

```python
    user_tweets = api.user_timeline(screen_name = user ,count=200)
    user_tweets = [tweet.text for tweet in user_tweets]
    user_tweets = clean_tweets(user_tweets)                                  
```

- Now for the analysis. Use a list comprehension to create a new list called `rating`. This should iterate over the `user_tweets` list, run the tweet through the `parse_tweet` function and then classify it (using `classifier.classify()`. If you can't figure it out, use the video in the hint below.

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_12.webm" type="video/webm">
Your browser does not support WebM video, try FireFox or Chrome
</video>
--- /hint --- --- /hints ---

- Your new `rating` list should now contain a large list with a mixture of `'negative'` and `'positive'` items. Write a few lines of code that will:
  - Count the percentage of `'negative'` strings in the `rating` list.
  - Print out that the user is naughty if the percentage is above 50%
  - Print out that the user is nice if the percentage is equal to or less than 50%
  - Optionally print out the accuracy of the algorithm.

If you're stuck then look at the video in the hint below.

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_13.webm" type="video/webm">
Your browser does not support WebM video, try FireFox or Chrome
</video>
--- /hint --- --- /hints ---

- You can complete your code by calling the function and giving it a user to collect tweets from. For example, adding this line to the end of your code.

```python
calculate_naughty(classifier, accuracy, 'coding2learn')
```