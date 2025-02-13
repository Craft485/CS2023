_author_ = "Colin Davis"
_credits_ = []
_email_ = "davis7cl@mail.uc.edu"

"""
The "Newton Find Zero" method works better for estimating both pi and the dottie number 
as it takes the same or fewer steps than the fixed point iteration approach
"""

# Return true if an only if the distance from f(x) to x is close enough (less than 1e-15)
def approx_fixed_point(f, x):
    return abs(f(x) - x) < 1e-15

def fixed_point_iteration(f, x = 1.0):
    """
    >>> from math import sin, cos
    >>> fixed_point_iteration(lambda x: sin(x) + x, 3.0)
    (3.141592653589793, 3)
    >>> fixed_point_iteration(lambda x: cos(x), 1.0) # Fixed point defining dottie number in 86 steps
    (0.7390851332151611, 86)
    """
    step = 0
    while not approx_fixed_point(f, x):
        x = f(x)
        step += 1
    return x, step

"""
# This is the implementation of newton_find_zero that is discussed in the resource linked on the assignment page.
# Once I had it written out I realized that it was very similiar to the fixed point iteration approach with the equation used being the only difference.
# Both versions I've written of this method get very close to the dottie number in only 4 steps, which leads it to fail the doc test.

def improve(update, close, guess = 1):
    steps = 0
    while not close(guess):
        steps += 1
        guess = update(guess)
    return guess, steps

def newton_update(f, df):
    return lambda x: x - f(x) / df(x)

def find_zero(f, df, guess = 1):
    return improve(newton_update(f, df), lambda x: abs(f(x)) < 1e-15, guess)
"""

def newton_find_zero(f, f_prime, guess):
    """
    >>> from math import sin, cos
    >>> newton_find_zero(lambda x: sin(x), lambda x: cos(x), 3.0)
    (3.141592653589793, 3)
    >>> newton_find_zero(lambda x: cos(x) - x, lambda x: -sin(x) - 1, 1.0) # Newtons's zero giving dottie in 7 steps
    (0.7390851332151606, 7)
    """
    # This mostly works, but gets super close to the dottie number before stopping 4 steps in
    # it does, however, manage to get pi
    step = 0
    x = guess
    while not (abs(f(x)) < 1e-15): # While we haven't met the tolerance
        step += 1
        x = x - (f(x) / f_prime(x)) # Get the next value of x
    return x, step

import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)