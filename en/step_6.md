## Cleaning up the tweets.

At the moment the tweets you have collected contain information we'd rather not include when running a sentiment analysis. This includes any @mentions, any urls and any punctuation. So the next step is to strip that information out of the tweets, leaving only the words and the emojis.

- Start by creating a new function called `clean_tweets`. This can go just above your `##EXECUTE THE PROGRAM` section.

```python
def clean_tweets(tweets):
```

- The easiest way to remove these strings from the tweets is to use regex. Go back up to the top of your code and add the following into your imports.

```python
import re
```

The collapsed section below provides details on how to use regex to remove words beginning with a certain string.

--- collapse ---
---
title: Removing strings based on their beginning
---
Here is a simple string.
```python
my_string = "The price of milk is £0.45 a pint"
```
Now image you wanted to remove price of milk.

- Start by removing the `£` sign, using the `re.sub` method to replace it with an empty string..

```python
re.sub(r'£', '', my_string)
```

- Next you can remove any character straight after the `£` sign, as long as it's not a whitespace character, using the `\S` pattern.

```python
re.sub(r'£\S', '', my_string)
```

- This leaves `'The price of milk is .45 a pint'`. By adding a `+` pattern after the `\S` you are searching for every character after the `£` sign, until a whitespace character is found.

```python
re.sub(r'£\S+', '', my_string)
```
--- /collapse ---

- Use regex to iterate over all the tweets in the list of tweets and remove all the `@mentions` and all the urls that start with `http`.

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_5.webm" type="video/webm">
Your browser does not support WebM video, try FireFox or Chrome
</video>

--- /hint --- --- /hints ---

Now you need to remove the punctuation. You can use the `translate` method to do this. Have a look at the collapsible section below if you need to learn how this is done.

--- collapse ---
---
title: Using `translate`
---
The `translate` method can be used to translate one character into another. The `translate` method needs to be provided with a dictionary of characters, where the key is the unicode point of the characters and the value is the character to be replaced with.

```python
>>> 'gold'.translate({ord('d'):'f'})
'gold'
>>>
```

If you wanted to translate all the ascii characters in a string into whitespace, it might take a while to create the dictionary. Luckily the `string` module and a dictionary comprehension can help out here.

```python
>>> import string
>>> s = 'Hello, here is a string!'
>>> s.translate({ord(char): ' ' for char in string.ascii_letters})
'     ,                 !'
>>>
```

There are other methods available in the `string` module.
```python
string.ascii_lowercase ##all the lower case characters
string.ascii_uppercase ##all the upper case characters
string.digits          ##all the digits
string.punctuation     ##all the punctuation symbols.
```
--- /collapse ---

- Now use the `translate` method and the `string` module to turn all the punctuation symbols into empty strings.

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_6.webm" type="video/webm">
Your browser does not support WebM video, try FireFox or Chrome
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
Your browser does not support WebM video, try FireFox or Chrome
</video>

--- /hint --- --- /hints ---
