## Reading the Twitter stream

In this step, you will learn how to select certain tweets from the stream, that can be analysed.

You need an easy way to categorise whether any particular tweet reflects a positive sentiment or a negative sentiment. This could be done by looking at words with positive and negative connotations. But words can have different meanings in different contexts. The word `bad` for instance could be deemed to be negative, but in the sentence `He's not a bad guy.` it takes on a positive meaning. Similarly `love` could be thought of as a positive word, except in sentences such as `I love watching children fall over.`

To get around this, you are going to categorise tweets using emojis. Emojis are fairly easy to categorise. For instance the presence of 😙 and ❤ in a tweet would generally indicate that it is a positive tweet. 😩 and 💔 would probably indicate negative tweets though.

- Start by creating two lists, one for positive and one for negative emojis. This can go at the end of the `naughty_and_nice.py` file you have created. [You can add more emojis than are shown here, if you like](https://unicode.org/emoji/charts/full-emoji-list.html){:target="_blank"}.

```python
##EMOJI DATA
pos_emojis = ['😙','❤','😍','💓','😗','☺','😊','😛','💕','😀','😃','😚']
neg_emojis = ['☹','😕','😩','😒','😠','😐','😦','😣','😫','😖','😞','💔','😢','😟']
```

--- collapse ---
---
title: Instructions if your text editor does not allow emojis
---
- Some text editors and IDEs don't allow emoji characters. IDLE, for instance, won't print emojis to the shell. If you are using IDLE, or another IDE that doesn't support emojis, then use therse lines instead.

```python
pos_emojis = [chr(uni) for uni in [128537, 10084, 128525, 128147, 128535, 9786, 128522, 128539, 128149, 128512, 128515, 128538]]
neg_emojis = [chr(uni) for uni in [9785, 128533, 128553, 128530, 128544, 128528, 128550, 128547, 128555, 128534, 128542, 128148, 128546, 128543]]
```

- This is essentially the same as using the emojis, but instead uses their **code point** which is then converted to the character.
--- /collapse ---

- You then need to create a list called `all_emojis` containing all the emojis, to be used in the search of tweets.

--- hints --- --- hint ---
You can combine lists together by concatonating them.
--- /hint --- --- hint ---
So to join two lists together, just use a `+` sign.
```python
new_list = old_list_1 + old_list_2
--- /hint --- --- hint ---
Here's the line you need
```python
all_emojis = pos_emojis + neg_emojis
```
--- /hint --- --- /hints ---


- Now you can start to fetch 200 tweets, but only if they are in English and contain one or more of the listed emojis.

```python
##FETCH SOME TWEETS
myStream.filter(track=all_emojis, languages=['en'])
```

- If you run this file and wait for it to finish running, you can switch into the shell, where typing `tweets[0]` will show you the first tweet. Similarly `tweets[200]` will show you the last tweet. Here's an example.

```python
>>> tweets[134]
'Chemistry tests change people 😕\n#science #knowledge #Chemistry https://t.co/9IhAi8nFKP'
>>>
```
