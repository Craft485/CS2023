"""
Slope: 0.36690066090066087
Intercept: 0.051219219219234446
RValue: 0.9978320351847708
"""

_author_ = "Colin Davis"
_credits_ = []
_email_ = "davis7cl@mail.uc.edu"

import numpy as np
from random import random

balls = range(1, 1001, 1)
emptyBins = []
for N in balls:
    bins = np.zeros(N)
    for _ in range(N):
        bins[int(N * random())] += 1
    emptyBins.append(len([x for x in bins if x == 0]))

from scipy import stats

binsRegress = stats.linregress(balls, emptyBins)

print(f'Slope: {binsRegress.slope}\nIntercept: {binsRegress.intercept}\nRValue: {binsRegress.rvalue}')

import matplotlib.pyplot as plt

plt.plot(balls, emptyBins)
plt.show()