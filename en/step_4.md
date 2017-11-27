## Reading the Twitter stream

In this step, you will learn how to select certain tweets that can be used in your sentiment analysis from the stream.

You need an easy way to categorise whether a particular tweet reflects a positive or a negative sentiment. This could be done by looking at words with positive and negative connotations. But words can have different meanings in different contexts. For instance, the word `bad` could be deemed to be negative, but in the sentence `He's not a bad guy.`, it takes on a positive meaning. Similarly, `love` could be thought of as a positive word, except in sentences such as `I love watching children fall over.`.

To get around this, you are going to categorise tweets using emojis. Emojis are fairly easy to categorise. For example, the presence of 😙 and ❤ in a tweet generally indicates that it is a positive tweet. On the other hand, 😩 and 💔 would probably indicate negative tweets.

- Go to the bottom of your `naughty_and_nice.py` file and create two lists, one for positive and one for negative emojis.

```python
##EMOJI DATA
pos_emojis = ['😙','❤','😍','💓','😗','☺','😊','😛','💕','😀','😃','😚']
neg_emojis = ['☹','😕','😩','😒','😠','😐','😦','😣','😫','😖','😞','💔','😢','😟']
```

[You can add more emojis than are shown here, if you like](https://unicode.org/emoji/charts/full-emoji-list.html){:target="_blank"}.

--- collapse ---
---
title: Instructions if your text editor does not allow emojis
---
Some text editors and IDEs don't allow emoji characters. IDLE, for instance, won't print emojis to the shell.

- If you are using IDLE, or another IDE that doesn't support emojis, then use these lines of code instead.

```python
pos_emojis = [chr(uni) for uni in [128537, 10084, 128525, 128147, 128535, 9786, 128522, 128539, 128149, 128512, 128515, 128538]]
neg_emojis = [chr(uni) for uni in [9785, 128533, 128553, 128530, 128544, 128528, 128550, 128547, 128555, 128534, 128542, 128148, 128546, 128543]]
```

This is essentially the same as using the emojis, but instead you use their **code points**, which are then converted to the characters.
--- /collapse ---

- You then need to create a list called `all_emojis` containing all the emojis to be used in your search through tweets.

--- hints --- --- hint ---
You can combine lists together by concatenating them.
--- /hint --- --- hint ---
To join two lists together, just use a `+` sign.
```python
new_list = old_list_1 + old_list_2
```
--- /hint --- --- hint ---
Here's the line you need:
```python
all_emojis = pos_emojis + neg_emojis
```
--- /hint --- --- /hints ---

- Now you can start to fetch 200 tweets, but only if they are in English and contain one or more of the listed emojis.

```python
##FETCH SOME TWEETS
myStream.filter(track=all_emojis, languages=['en'])
```

- Save and run your file, and wait for it to finish running.

- Now you can switch to the shell, where typing `tweets[0]` will show you the first tweet. Similarly, `tweets[200]` will show you the last tweet. Here's an example:

```python
>>> tweets[134]
'Chemistry tests change people 😕\n#science #knowledge #Chemistry https://t.co/9IhAi8nFKP'
>>>
```
