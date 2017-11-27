## Sorting tweets

Now that you have a growing list of recent random tweets, you need to categorise each tweet according to whether it has a positive sentiment (nice) or a negative sentiment (naughty). You will do this by seeing which tweets contain positive emojis and which contain negative ones.

Let's tackle the positive tweets first: you can use Python's `set` data structure again to see which tweets have positive emojis. If the `set` of a tweet contains the same characters as the `set` of positive emoji, then the tweet can be classified as positive. In set theory, this is called the **intersection**, and you can use the Python `&` operator to find it.

- Create a function called `sort_tweets` that takes the list of tweets as an argument.
- Inside the function, use `set` to build a list of all tweets that contain a positive emoji. You could do this using another list comprehension, or just a loop if you prefer. If you're completely stumped, then have a look at the section below.

--- collapse ---
---
title: Set intersections on strings
---
You can easily find out whether a string contains any characters found in another string by using sets. For instance, here are two strings:
```python
text = "I hope it's not ☔"
weather = "☔☀⚡☁"
```
Now, let's see if the `text` string contains any emoji that indicates weather. First, both strings need to become sets.
```python
text_set = set(text)
weather_set = set(weather)
```
The two sets look like this:
```python
{'☔', 'e', 'I', 'i', 't', "'", 'p', 'n', 's', ' ', 'o', 'h'}
{'☔', '☁', '☀', '⚡'}
```
You can see the intersection of the two sets easily:
```python
>>> set(text) & set(weather)
{'☔'}
>>>
```

So to see if two strings contain any of the same characters, you just need to see whether their set intersections are empty. For example:

```python
if set(text) & set(weather):
	print("Text is about the weather")
```
--- /collapse ---

- You can do the same with the negative tweets now, and make sure to wrap it all in the `sort_tweets` function. Have a look at the hint below if you need help with this.

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_8.webm" type="video/webm">
Your browser does not support WebM video, so try FireFox or Chrome.
</video>

--- /hint --- --- /hints ---

You're also going to want to make the `sort_tweets` function remove any emojis that are in the tweets, since you want the sentiment analysis to be conducted on words alone and not be influenced by emojis.

- You can use regex to remove any character that is not an ASCII character (i.e. the normal set that you see on a standard keyboard) from the both groups of tweets. This will remove the emojis, which we no longer need, since the tweets have now been classified according to sentiment.

```python
positive_tweets = [re.sub(r'[^\x00-\x7F]+','', tweet) for tweet in positive_tweets]
negative_tweets = [re.sub(r'[^\x00-\x7F]+','', tweet) for tweet in negative_tweets]
```

- To finish off the `sort_tweets` function, have it return the positive and negative tweets.

- At the bottom of the file, add a line to call this function, saving its output as `pos_tweets` and `neg_tweets`.

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_9.webm" type="video/webm">
Your browser does not support WebM video, so try FireFox or Chrome.
</video>

--- /hint --- --- /hints ---
