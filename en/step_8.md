## Parsing tweets

For the sentiment analysis program to be able to categorise a tweet, the tweet's text needs to be in a particular form. This is called string parsing. In the case of the natural-language processor you will be using, each tweet needs to be stripped of words that have no  sentiment value. This will just leave useful words that can then be placed in a dictionary which will look a little like this:

```python
{'why': True, 'want': True, 'talk': True, 'happy': True, 'today': True, 'hello': True}
```

- Start by importing two more modules where your other `import` statements are.

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
```

- Then create a new function called `parse_tweets`. The function can take any string as a parameter.

```python
def parse_tweets(words):
```

- The first line of code in the function should change all the characters in the string into lower case.

```python
def parse_tweets(words):
	words = words.lower()
```

- Next you are going to `tokenize` the words. This will split them up into a list.
```python
def parse_tweets(words):
	words = words.lower()
	words = word_tokenize(words)
```

Then you can use a feature of `nltk` called `stopwords`. These are words like 'i', 'me', and 'my' that don't carry any meaning for our sentiment analysis. You can see a list of all the stop-words by typing the following into your shell:

```python
>>> from nltk.corpus import stopwords
>>> stopwords.words('english')
```

- To have your function remove the stop-words, use a list comprehension to iterate over all the items in the `words` list, and only keep words if they're not among the `stopwords`. Have a look at the video below to get a better idea of how to do this.

<video width="560" height="315" controls>
<source src="images/vid_10.webm" type="video/webm">
Your browser does not support WebM video, so try FireFox or Chrome.
</video>

- To finish off the `parse_tweets` function, each word needs adding into a dictionary where the word is the key and `True` is the value. Then have the function return the dictionary.

Check out the collapsible section below to see the complete code for the function.

--- collapse ---
---
title: Your complete `parse_tweets` function
---

```python
def parse_tweets(words):
    words = words.lower()
    words = word_tokenize(words)
    words = [word for word in words if word not in stopwords.words("english")]
    word_dictionary = dict([(word, True) for word in words])
    return word_dictionary
```
--- /collapse ---
