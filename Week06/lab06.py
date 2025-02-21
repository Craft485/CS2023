## Required Questions: Linked Lists ##
## Use the Linked List ADT defined below

_author_ = "Colin Davis"
_credits_ = []
_email_ = "davis7cl@mail.uc.edu"

#RQ1
def has_prefix(s, prefix):
    """Returns whether prefix appears at the beginning of linked list s.

    >>> x = link(3, link(4, link(6, link(6))))
    >>> print_link(x)
    3 4 6 6
    >>> has_prefix(x, empty)
    True
    >>> has_prefix(x, link(3))
    True
    >>> has_prefix(x, link(4))
    False
    >>> has_prefix(x, link(3, link(4)))
    True
    >>> has_prefix(x, link(3, link(3)))
    False
    >>> has_prefix(x, x)
    True
    >>> has_prefix(link(2), link(2, link(3)))
    False
    """
    if prefix == empty: # Edge case
        return True
    
    sFlat = flat(s)

    preFlat = flat(prefix)

    if len(preFlat) > len(sFlat):
        return False
    
    sSublist = sFlat[0 : len(preFlat)]
    for i in range(len(preFlat)):
        if sSublist[i] != preFlat[i]:
            return False
    
    return True # Default case


#RQ2
def has_sublist(s, sublist):
    """Returns whether sublist appears somewhere within linked list s.

    >>> has_sublist(empty, empty)
    True
    >>> aca = link('A', link('C', link('A')))
    >>> x = link('G', link('A', link('T', link('T', aca))))
    >>> print_link(x)
    G A T T A C A
    >>> has_sublist(x, empty)
    True
    >>> has_sublist(x, link(2, link(3)))
    False
    >>> has_sublist(x, link('G', link('T')))
    False
    >>> has_sublist(x, link('A', link('T', link('T'))))
    True
    >>> has_sublist(link(1, link(2, link(3))), link(2))
    True
    >>> has_sublist(x, link('A', x))
    False
    """
    if sublist == empty: # Edge case
        return True

    sFlat = flat(s)
    subFlat = flat(sublist)

    if len(subFlat) > len(sFlat):
        return False

    possibleSubArrayStartPoints = [ x for x in range(len(sFlat) - len(subFlat)) ]
    for point in possibleSubArrayStartPoints:
        sub_of_s = sFlat[point : point + len(subFlat)]
        sub_links = BuildLinkFromList(sub_of_s)
        if (has_prefix(sub_links, sublist)):
            return True
        
    return False # Default case


#RQ3
def has_kitty_gene(dna):
    """Returns whether the linked list dna contains the CATCAT gene as a sublist.

    >>> dna = link('C', link('A', link('T')))
    >>> dna = link('C', link('A', link('T', link('G', dna))))
    >>> print_link(dna)
    C A T G C A T
    >>> has_kitty_gene(dna)
    False
    >>> end = link('T', link('C', link('A', link('T', link('G')))))
    >>> dna = link('G', link('T', link('A', link('C', link('A', end)))))
    >>> print_link(dna)
    G T A C A T C A T G
    >>> has_kitty_gene(dna)
    True
    >>> has_kitty_gene(end)
    False
    """
    CATCAT = link('C', link('A', link('T', link('C', link('A', link('T'))))))
    return has_sublist(dna, CATCAT)


#RQ4
# A set of coins makes change for n if the sum of the values of the coins is n. 
# For example, if you have 1-cent, 2-cent and 4-cent coins, the following sets make change for 7:
#
# 7 1-cent coins
# 5 1-cent, 1 2-cent coins
# 3 1-cent, 2 2-cent coins
# 3 1-cent, 1 4-cent coins
# 1 1-cent, 3 2-cent coins
# 1 1-cent, 1 2-cent, 1 4-cent coins
# Thus there are 6 ways to make change for 7. Write a function count_change that takes a positive integer n 
# and a linked list of the coin denominations and returns the number of 
# ways to make change for n using these coins:

def count_change(amount, denominations, permutations: list = [], currDenominationIndex = 0, firstCall = True):
    """Returns the number of ways to make change for amount where denominations is a linked list of coins
       in descending sorted order.
    >>> denominations = link(50, link(25, link(10, link(5, link(1)))))
    >>> print_link(denominations)
    50 25 10 5 1
    >>> count_change(7, denominations)
    2
    >>> count_change(100, denominations)
    292
    >>> denominations = link(16, link(8, link(4, link(2, link(1)))))
    >>> print_link(denominations)
    16 8 4 2 1
    >>> count_change(7, denominations)
    6
    >>> count_change(10, denominations)
    14
    >>> count_change(20, denominations)
    60
    """
    # This solution probably isn't the best for this situation, 
    # but I had to do something similar for a personal project and wanted to see if 
    # I could apply the same thinking here

    # My idea for this question is to think of its as a sort of graph / tree
    # Each denomination will act as a root node, 
    # we can then recurse to get every permutation of coins that include the current denomination
    # and that sum to the given amount

    if firstCall: # If current stack call is top of the recursion chain
        permutationCount = 0
        # Treat any denominations that are less than or equal to the amount as valid starting nodes
        validDenominations = [ x for x in flat(denominations) if x <= amount ]
        # Recurse from each source node to build permutations
        for i in range(len(validDenominations)):
            permutationCount += count_change(amount, validDenominations, [[validDenominations[i]]], i, False)
        return permutationCount
    else:
        newPermutations = []
        # Sink nodes are defined by permutations that add up to "amount"
        sinkNodeCount = 0
        for permutation in permutations:
            currSum = sum(permutation)
            if currSum == amount:
                sinkNodeCount += 1
                continue
            # Find denominations that can still be added to the current permutation
            validDenominations = [ x for x in denominations[currDenominationIndex:] if amount >= currSum + x ]
            for denomination in validDenominations:
                newPermutation = sorted(permutation + [ denomination ])
                if newPermutation not in newPermutations: # Before adding the new permutation, make sure its unique
                    newPermutations.append(newPermutation)
        if len(newPermutations) > 0:
            sinkNodeCount += count_change(amount, denominations, newPermutations, currDenominationIndex, False)
        return sinkNodeCount





# Linked list ADT
# Interface Definitions and Implementations
empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)

# Couple of helper functions for some actions that I intend to do multiple times

def flat(s):
    sFlat = []
    ref = s
    while ref[0] != empty and ref[1] != empty:
        sFlat.append(ref[0])
        ref = rest(ref)
    sFlat.append(ref[0]) # Add last link
    return sFlat

def BuildLinkFromList(lst):
    rl = lst[::-1] # Reverse the list so that when the link is built we keep the same order of data
    l = empty
    for x in rl:
        l = link(x, l)
    return l

import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)
