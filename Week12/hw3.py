"""
My solution for this assignment was to get various permutations of the letters than made up the step word in order to search for possible annagrams
This solution was sped up by checking if the partial annagram existed somewhere in the initial dataset
This knowledge can tell me if the current permutation isn't going to lead me to anything, and therefore I don't need to continue building it

Even with this speed up, it can still take a bit for longer words to compute. However, I can't really see another way for significantly speeding up this process
"""

_author_ = "Colin Davis"
_credits_ = []
_email_ = "davis7cl@mail.uc.edu"

url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()
wordsCombined = ' '.join(words)

def annagram(currWord: str, remainingLetters: list[str]) -> list[str]:
    if len(remainingLetters) == 0: 
        return [currWord]
    result = []
    for i in range(len(remainingLetters)):
        nextWord = currWord + remainingLetters[i]
        if nextWord not in wordsCombined:
            continue # If we can confirm that the next permutation isn't going to lead anywhere, then theres no point in following that path
        nextLetters = remainingLetters[:]
        nextLetters.remove(remainingLetters[i])
        for x in annagram(nextWord, nextLetters):
            result.append(x)
    return result

def allsteps(word: str) -> list[str]:
    '''
    >>> allsteps("APPLE")
    ['ALEPPO', 'APPEAL', 'CAPPLE', 'DAPPLE', 'LAPPED', 'LAPPER', 'LAPPET', 'PALPED', 'PAPULE', 'RAPPEL', 'UPLEAP']
    >>> allsteps("UC")
    ['CUB', 'CUD', 'CUE', 'CUM', 'CUP', 'CUR', 'CUT', 'LUC', 'UCA']
    >>> allsteps("BEARCAT")
    ['ACERBATE', 'BACTERIA', 'BRACCATE', 'BRACTEAL', 'CARTABLE', 'SCABRATE']
    '''
    steps = [word + alphabet[i] for i in range(len(alphabet))]
    # print(steps)
    results = []
    for j in range(len(steps)):
        letters = [c for c in steps[j]]
        for x in annagram('', letters): # Recursively compute every annamgram for the current step word
            if x in words and x not in results:
                results.append(x)
    results.sort()
    # print(results)
    # print(len(results))
    return results

import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True) 