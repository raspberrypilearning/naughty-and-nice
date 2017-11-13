## Parsing tweets

For the program to be able to categorise a tweet, the text needs to be in a particular form. This is called string parsing. In the case of the natural language processer you will be using, each tweet needs stripping of words that have no real sentiment, and then placing in a dictionary that will look a little like this:

```python
{'why': True, 'want': True, 'talk': True, 'happy': True, 'today': True, 'hello': True}
```

- Start by importing a couple more modules, up where your other imports are.

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
```

- Then create a new function called `parse_tweets`. The function can take any stringg as a parameter.

```python
def parse_tweets(words):
```

- The first line of code in the function, should change all the characters in the string to lower case.

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

- Next you can use a feature of `ntlk` called `stopwords`. These are words like 'i', 'me', and 'my' that don't really carry any meaning. You can see all the `stopwords` by typing the following into your shell.

```python
>>> from nltk.corpus import stopwords
>>> stopwords.words('english')
```

- To remove the stopwords, use a list comprehension to iterate over all the items in the `words` list, and only add words if they're not in the `stopwords`. Have a look at the video below to get a better idea of how to do this.

<video width="560" height="315" controls>
<source src="images/vid_10.webm" type="video/webm">
Your browser does not support WebM video, try FireFox or Chrome
</video>

- To finish off this function, each word needs adding into a dictionary, where the word is the `key` and `True` is the value. This dictionary can then be returned. Your entire function will now look like this:

```python
def parse_tweets(words):
    words = words.lower()
    words = word_tokenize(words)
    useful_words = [word for word in words if word not in stopwords.words("english")]
    word_dictionary = dict([(word, True) for word in useful_words])
    return word_dictionary
```
