_author_ = "Colin Davis"
_credits_ = []
_email_ = "davis7cl@mail.uc.edu"

#RQ1
class Cheer():
    """
    >>> UC = Cheer("Bearcats")
    >>> for c in UC:
    ...     print(c)
    ...
    Give me an B
    Give me an e
    Give me an a
    Give me an r
    Give me an c
    Give me an a
    Give me an t
    Give me an s
    """
    def __init__(self, text):
        self.data = text

    def __iter__(self):
        self.currCharIndex = 0
        return self
    
    def __next__(self):
        if self.currCharIndex >= len(self.data):
            raise StopIteration
        val = self.data[self.currCharIndex]
        self.currCharIndex += 1
        return "Give me an " + val

#RQ2
class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    def __init__(self, N):
        self.data = N

    def __iter__(self):
        self.curr = self.data
        return self
    
    def __next__(self):
        if self.curr < 0:
            raise StopIteration
        val = self.curr
        self.curr -= 1
        return val 

##############
# Generators #
##############

# RQ3a
def evens():
    """A generator function that yields the infinite sequence of all even natural
    numbers, starting at 1.

    >>> m = evens()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    n = 0
    while True:
        n += 2
        yield n
        
# RQ3b        
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    n = 0
    while True:
        n += 1
        yield n
        
#RQ4
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]
    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    for n in s:
        yield n * k

# RQ5
def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    while n >= 0:
        yield n
        n -= 1

# RQ6
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    while True:
        yield n
        if n == 1:
            return
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1

import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)