## Storing tweets

The more data you have, the more accurate your sentiment analysis will be. At the moment, you have 201 tweets, which is not really enough. However, collecting thousands of tweets in one go would take ages, and the list of tweets would be emptied each time you run the program. For this reason you're going to save the tweets into a file, so that with each run of your program, your data set will grow.

- In the directory in which you saved your Python file, create a new empty file called `tweets.txt`. This is where the fetched tweets will be stored.

- Now define a new function called `store_tweets` at the bottom of your file. The function will have two parameters: the `file` to store the data in, and the `tweets` list you have created.

```python
def store_tweets(file, tweets):
```

Your `store_tweets` function needs to perform these steps:
1. Open the `file` file passed in as an argument
1. Load all tweets that are in this file
1. Combine these tweets with the ones in the `tweets` list, which were more recently collected
1. Duplicate tweets should be removed
1. The combined old and new tweets should be written back into the file

The first time you run the program, `tweets.txt` will be empty, but it will soon contain **a lot** of tweets.
	
- If you're confident about how to do this, then have a go. If not, you might find the sections below helpful.

--- collapse ---
---
title: Opening a file and reading it into a list
---
- To open a file, you first need to create a file object that contains all the file's data.
```python
with open('filename.txt', 'r') as f:
```

**If you are using Windows**, you may have issues if you do not specify an encoding type. Use this code instead:
```python
with open('filename.txt', 'r', encoding='utf8') as f:
```

- To read each line of the file into a list, you can use `readlines`.
```python
with open('filename.txt', 'r') as f:
	my_list = f.readlines()
```
--- /collapse ---

- In your function, open up the `file` file and load all the data into a list called `old_tweets`.

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_2.webm" type="video/webm">
Your browser does not support WebM video, so try FireFox or Chrome.
</video>

--- /hint --- --- /hints ---

- Now you need to merge the two sets of tweets into a single list, so the ones you have just collected from the stream and the ones stored in the file are combined. This is easy to do in Python, as you can simply add them together.

```python
all_tweets = old_tweets + tweets
```

If you run the program fairly often, there will probably be duplicate tweets. These need to be removed. **Sets** are great for removing duplicate items from a list. Have a look at the collapsible section below to see how to use them.

--- collapse ---
---
title: Removing duplicates items from a list
---
In Python, a set is an unordered collection of unique items. By its very definition it can't have duplicates within it. Here is an example of a Python set:

```python
>>> my_set = {1,2,3,4}
```

If you try and add duplicates, you'll see that they vanish.

```python
>>> my_set = (1,2,3,4,1,2,3,4}
>>> print(my_set)
{1, 2, 3, 4}
>>>
```

So to remove duplicates from a list, you just need to turn the list into a set, and then back into a list again.

```python
>>> my_list = [1,2,3,4,1,2,3,4]
>>> my_list = list(set(my_list))
>>> print(my_list)
[1,2,3,4]
>>>
```
--- /collapse ---

- Remove the duplicates from the `all_tweets` list.

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_3.webm" type="video/webm">
Your browser does not support WebM video, so try FireFox or Chrome.
</video>

--- /hint --- --- /hints ---

There's one small problem with the current list of `all_tweets`. Some people like to place `newlines` into their tweets — these need to be removed.

- Add the following line to replace all newlines (`\n`) within a tweet with an empty string (`''`), and then add a single newline to the end.

```python
all_tweets = [tweet.replace('\n','')+"\n" for tweet in all_tweets]
```

+ Lastly, you need to write all the tweets back into the file.

Have a look at the collapsible section below if you need help with doing this.

--- collapse ---
---
title: Write a list to a file
---
- First you need to open a file in a writable mode:
```python
with open('tweets.txt', 'w') as f:
```

**If you are using Windows***, you may have issues if you do not specify an encoding type. Use this code instead:

```python
with open('tweets.txt', 'w', encoding='utf8') as f:
```

- You can then use the `writelines` function to write the contents of the list into the file.

```python
with open('tweets.txt', 'w') as f:
	f.writelines(all_tweets)
```
--- /collapse ---

- Finish off the function by returning the `all_tweets` list.

- Call the function at the end of your program, and save its output as `tweets`.

--- hints --- --- hint ---
<video width="560" height="315" controls>
<source src="images/vid_4.webm" type="video/webm">
Your browser does not support WebM video, so try FireFox or Chrome
</video>

--- /hint --- --- /hints ---

- To test if your code works, run the program and then type the following into the shell:

```python
store_tweets('tweets.txt', tweets)
```

- If everything is correct, the `tweets.txt` file should now contain a few hundred tweets.
