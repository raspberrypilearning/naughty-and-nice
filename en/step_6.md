## Cleaning up the tweets

At the moment, the tweets you have collected contain information we don't want to include in the sentiment analysis: @mentions, URLs, and punctuation. So the next step is to strip the tweets of that information, leaving only words and emojis.

- Start by creating a new function called `clean_tweets`. It can go just above your `##EXECUTE THE PROGRAM` section.

```python
def clean_tweets(tweets):
```

- The easiest way to remove the unnecessary strings from the tweets is to use **regular expressions (or regex)**. Go to the top of your program, and add the `re` module to your imports:

```python
import re
```

The collapsible section below provides details on how to use regex to remove words beginning with a certain string.

--- collapse ---
---
title: Removing strings based on their beginning
---
Here is a simple string:
```python
my_string = "The price of milk is £0.45 a pint"
```
Now imagine you wanted to remove the `£0.45` from this string.

- Start by removing the `£` sign, using the `re.sub` method to replace it with an empty string.

```python
re.sub(r'£', '', my_string)
```

The `r` before the string ensures that the string is treated as a **raw string literal**. Don't worry too much about why it is needed, but if you want to learn more, then have a look at [the documentation here](https://docs.python.org/3.6/reference/lexical_analysis.html#string-and-bytes-literals).

- Next, you can remove any character straight after the `£` sign, as long as it's not a whitespace character, using the `\S` pattern.

```python
re.sub(r'£\S', '', my_string)
```

- This leaves `'The price of milk is .45 a pint'`. Adding a `+` pattern after the `\S` will remove every character after the `£` sign until a whitespace character is encountered.

```python
re.sub(r'£\S+', '', my_string)
```
--- /collapse ---

- Use regex to iterate over all the tweets in the list of tweets and remove all @mentions, as well as all URLs that start with 'http'.

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_5.webm" type="video/webm">
Your browser does not support WebM video, so try FireFox or Chrome.
</video>

--- /hint --- --- /hints ---

Now you need to remove the punctuation. You can use the `translate` method to do this. Have a look at the collapsible section below if you need to learn how this works.

--- collapse ---
---
title: Using `translate`
---
The `translate` method can be used to translate one character into another. It needs to be provided with a dictionary of characters, where the key is the **Unicode** point of the character (`ord('d')` for example), and the value is the character with which you want to replace it.

```python
>>> 'gold'.translate({ord('d'):'f'})
'golf'
>>>
```

If you wanted to translate all the ASCII characters in a string into whitespace, it might take a while to create the dictionary. Luckily, the `string` module and a dictionary comprehension can help out here.

```python
>>> import string
>>> s = 'Hello, here is a string!'
>>> s.translate({ord(char): ' ' for char in string.ascii_letters})
'     ,                 !'
>>>
```

There are other methods available in the `string` module:
```python
string.ascii_lowercase ##all the lower case characters
string.ascii_uppercase ##all the upper case characters
string.digits          ##all the digits
string.punctuation     ##all the punctuation symbols.
```
--- /collapse ---

- Use the `translate` method and the `string` module to turn all the punctuation symbols into empty strings.

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_6.webm" type="video/webm">
Your browser does not support WebM video, so try FireFox or Chrome.
</video>

--- /hint --- --- /hints ---

- Finish off by using the `rstrip()` method to remove the newlines from the end of each of the tweets, then return the tweets.

```python
tweets = [tweet.rstrip() for tweet in tweets]
```

- You can now test your code out by calling the function. Check the video below if you're not sure how to do that.

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_7.webm" type="video/webm">
Your browser does not support WebM video, so try FireFox or Chrome.
</video>
--- /hint --- --- /hints ---
