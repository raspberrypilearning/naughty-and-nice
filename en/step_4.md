## Reading the Twitter steam

In this step, you will learn how to select certain tweets from the stream, that can be analysed.

You need an easy way to categorise whether any particular tweet reflects a positive sentiment or a negative sentiment. This could be done by looking at words with positive and negative conetations. But words can hav different meanings in different contexts. The word `bad` for instance could be deemed to be negative, but in the sentence `He's not a bad guy.` it takes on a positive meaning. Similarly `love` could be thought of as a positive word, except in sentences such as `I love watching children fall over.`

To get around this, you are going to categorise tweets using emojis. Emojis are fairly easy to categorise. For instance the presence of 😙 and ❤ in a tweet would generally indicate that it is a positive tweet. 😩 and 💔 would probably indicate negative tweets though.

- Start by creating two strings, one for positive and one for negative emojis. This can got at the end of the `naughty_and_nice.py` file you have created. You can add more emojis than are shown here, if you like.

```python
##EMOJI DATA
pos_emojis = '😙❤😍💓😗☺😊😛💕😀😃😚'
neg_emojis = '☹😕😩😒😠😐😦😣😫😖😞💔😢😟'
```

- You then need to create a list that contains all of the `pos_emojis` and all of the `neg_emojis`

```python
all_emojis = list(pos_emojis + neg_emojis)
```

- Now you can start to fetch 200 tweets, but only if they are in English and contain one or more of the listed emojis.

```python
##FETCH SOME TWEETS
myStream.filter(track=all_emojis, languages=['en'])
```

- If you run this file and then switch into the shell, typing `tweet[0]` will show you the first tweet. similarly `tweets[200]` will show you the last tweet. Here's an example.

```python
>>> tweets[134]
'Chemistry tests change people 😕\n#science #knowledge #Chemistry https://t.co/9IhAi8nFKP'
>>>
```
