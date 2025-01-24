"""
Write a python program from scratch (with no starting code) which includes a function called "egypt", which has two integer arguments, say p and q, and uses the greedy approach. 
Your function should return a string representing a sum of unit fractions, with sum equal to p/q.
"""

def egypt(n: int, d: int) -> str:
    """
    >>> egypt(3,4)
    '1/2 + 1/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12'

    # Partial credit will be given for code that passes the two given doctests. 
    # For full credit on HW1 you should test your solutions to egypt(103,104) and  egypt(123,124)
    # These are more difficult and may require you to develop faster, more efficient code.

    >>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112'
    >>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424'
    """
    result: list[str] = [] # Keep track of unit fractions

    # Perform the greedy algorithm as outlined
    while n != 0:
        # NOTE: Simply using ceil(d / n) won't work for the larger values.
        #       Instead, we need to find a way to use integer division (to handle the large values)
        #       while not losing precision from the floor function that is applied from integer division.
        #       This can be achieved by taking the sum of the numerator and denominator, subtracting one,
        #       then performing integer division with the original numerator as the new denominator
        unit = (n + d - 1) // n
        result.append(f'1/{unit}')
        # Update n and d (equivalent to  (n / d) - unit but preserving the individual numerator and denominator)
        n = n * unit - d
        d *= unit
    return ' + '.join(result)

import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)