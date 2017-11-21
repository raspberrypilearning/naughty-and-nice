## Sorting tweets

Now that you have an ever growing list of recent tweets, you need to categorise them into whether each tweet has a positive sentiment (nice), or a negative sentiment (naughty). You can do this by seeing which tweets have positive emojis in them and which tweets have negative emojis in them.

Tackling the positive tweets first, you can again use Python's `set` data structure to see which tweets have positive emojis in them. If the `set` of a tweet contains the same characters as the `set` of positive emoji, then the tweet can be classified as positive. In set theory this is called the `intersection` and in Python you can use the `&` operator to find this.

- Create a function called `sort_tweets` that takes the list of tweets as an argument.
- Now, using `set` build a list of all tweets that contain a positive emoji. You could do this using another list comprehension, or just a looop if you prefer. If you're completely stumped then have a look at the section below.

--- collapse ---
---
title: Set intersections on strings.
---
You can easily find out if a string contains any characters in another string, by using sets. For instance, here are two strings.
```python
text = "I hope it's not ☔"
weather = "☔☀⚡☁"
```
Now, let's see if the `text` contains any emoji that would indicate weather. First both strings need to become sets.
```python
text_set = set(text)
weather_set = set(weather)
```
Now the two sets look like this
```python
{'☔', 'e', 'I', 'i', 't', "'", 'p', 'n', 's', ' ', 'o', 'h'}
{'☔', '☁', '☀', '⚡'}
```
You can see the intersection of the two sets fairly easily.
```python
>>> set(text) & set(weather)
{'☔'}
>>>
```

So to see if two strings contain any of the same characters, you just need to see if their set intersections are empty or no. For example:

```python
if set(text) & set(weather):
	print("Text is about the weather")
```
--- /collapse ---

- You can do the same with the negative tweets now, and wrap it all in a function called `sort_tweets`. Have a look at the hint below if you need help with this.

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_8.webm" type="video/webm">
Your browser does not support WebM video, try FireFox or Chrome
</video>

--- /hint --- --- /hints ---

To finish off this function, you're also going to want to remove any emoji that are in the positive and negative tweets. You want the sentiment analysis to be conducted on words alone, and not influenced by any emoji in the text.

- You can use regex to remove any character that is not an ASCII character (the normal set that you see on a standard keyboard), from the positive and negative tweets. This will remove the emoji, which we no longer need, as the tweets have been classified as positive or negative.

```python
positive_tweets = [re.sub(r'[^\x00-\x7F]+','', tweet) for tweet in positive_tweets]
negative_tweets = [re.sub(r'[^\x00-\x7F]+','', tweet) for tweet in negative_tweets]
```

- Then at the end you can return the positive and negative tweets.

- Finally, at the end of the file, you can add a line to call this function, saving it's output as `pos_tweets` and `neg_tweets`

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_9.webm" type="video/webm">
Your browser does not support WebM video, try FireFox or Chrome
</video>

--- /hint --- --- /hints ---
