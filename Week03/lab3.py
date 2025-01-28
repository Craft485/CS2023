# CS2023 - Lab 3 Required Questions 
# All functions should be written using recursion.

_author_ = "Colin Davis"
_credits_ = []
_email_ = "davis7cl@mail.uc.edu"

# RQ1
def doubletime(i: int, n: int) -> int:
    """Returns the result of repeatedly doubling the number i a total of n times
    >>> doubletime(3, 1)
    6
    >>> doubletime(2, 0)
    2
    >>> doubletime(2, 9)
    1024
    """
    return i if n == 0 else doubletime(2 * i, n - 1)

# RQ2
def skip2_add(n: int) -> int:
    """ Takes a number x and returns x + x-3 + x-6 + x-9 + ... + 0.

    >>> skip2_add(5)  # 5 + 2  + 0
    7
    >>> skip2_add(10) # 10 + 7 + 4 + 1 + 0
    22
    """
    return 0 if n <= 0 else n + skip2_add(n - 3)

# RQ3
def a(n: int) -> int:
    """Return the number in the sequence defined by a(1) = 1;
    a(n) = (3/2)*a(n-1) if a(n-1) is even; a(n) = (3/2)*(a(n-1)+1) if a(n-1) is odd.
    (see, http://oeis.org/A070885)

    >>> a(1)
    1
    >>> a(2) 
    3
    >>> a(3)
    6
    >>> a(10)
    123
    """
    if n == 1: # a(1)
        return 1
    elif a(n - 1) % 2 == 0: # a(n) when a(n - 1) is even
        return int((3/2) * a(n - 1))
    else: # a(n) when a(n - 1) is odd
        return int((3/2) * (a(n - 1) + 1))

#RQ4 - Note: I had to add another parameter for this to work with recursion, I can't see any other way to make this work but it still felt wrong
def paths(m: int, n: int, permutations: list[list[int]] = [[0, 0]]) -> int:
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    >>> paths(2, 2)
    2
    >>> paths(3, 3)
    6
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 or n == 1: # If there is ever a single column or a single row, then there is only 1 possible path
        return 1
    newPerms = []
    sinkNodeCount = 0 # Keep track of the number of paths that have already reached the opposite corner

    for [row, col] in permutations:
        if row == m - 1 and col == n - 1: # This path is already done
            newPerms.append([row, col])
            sinkNodeCount += 1
            continue
        if row + 1 <= m - 1: # Check if we can go up from here
            newPerms.append([row + 1, col])
        if col + 1 <= n - 1: # Check if we can go right from here
            newPerms.append([row, col + 1])
    return len(newPerms) if sinkNodeCount == len(permutations) else paths(m, n, newPerms)

import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)