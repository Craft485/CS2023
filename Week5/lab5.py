## Lab 5: Required Questions - Dictionaries  ##

_author_ = "Colin Davis"
_credits_ = []
_email_ = "davis7cl@mail.uc.edu"

# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    for [k, v] in dict2.items(): # For each key value pair in the second dictionary, add them to the first
        dict1[k] = v
    return dict1

# RQ2
def counter(message: str):
    """ Returns a dictionary where the keys are the words in the message, and each
    key is mapped (has associated value) equal 
    to the number of times the word appears in the message.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    words = message.split(' ')
    freq = {}
    for word in words: # For each word in the string, keep a counter of how many times the word occurs in the string
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

# RQ3
def replace_all(d, x, y):
    """ Returns a dictionary where the key/value pairs are the same as d, 
    except when a value is equal to x, then it should be replaced by y.
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> d2= replace_all(d, 3, 'poof')
    >>> d2 == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    for key in d: # For each key in the dictionary, check if its value matches x and replace with y if so
        if d[key] == x:
            d[key] = y
    return d

# RQ4
def sumdicts(lst):
    """ 
    Takes a list of dictionaries and returns a single dictionary which contains all the keys/value pairs found in list. And 
    if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
    as the value mapped for that key
    >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
    >>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
    True
    """
    result = {}
    for dict in lst: # For each dictionary
       for key in dict: # For each entry in the current dictionary
            if key in result: # If the result already contains the key, combine the values
               result[key] += dict[key]
            else: # Otherwise, add the new key to the result
                result[key] = dict[key]
    return result

#RQ5

#Here is starter code that is explained in the Interactive Worksheet

def build_successors_table():
    """Return a dictionary: keys are words; values are lists of successor words. By default, we set the first word in tokens to be a successor to "."
    """
    f = open("shakespeare.txt", "r", encoding="ascii")
    tokens = f.read().split()
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = []
        table[prev] += [word]
        prev = word
    return table

def construct_tweet(word, table):
    """Returns a string that is a random sentence starting with word, and choosing successors from table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        result += word + ' '
        word = random.choice(table[word])
    return result + word

def random_tweet():
    import random
    tweet_table = build_successors_table()
    return construct_tweet(random.choice(tweet_table['.']), tweet_table)
   
def middle_tweet():
    """ Calls the function random_tweet() 5 times. Modify this code to 
    returns one single string which has length in middle value of the 5.
    My experiments showed that with 5 random samples you should usually
    get a tweet that is in range of 60-100 characters. One of the following tests
    may sometimes fail.
    >>> len(middle_tweet()) > 60
    True
    >>> len(middle_tweet()) < 100
    True
    """
    # Generate a list of string lengths from 5 random tweets, the actual contents of the string doesn't matter
    lst = [len(random_tweet()) for _ in range(5)]
    lst.sort() # Sort the list in ascending order
    return 'a' * lst[3] # Return a string with the same length as the original tweet

import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)