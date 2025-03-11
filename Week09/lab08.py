## Lab 8: Trees  ##
# Four Required Questions 


# pyTunes
def make_pytunes(username):
    """Return a pyTunes tree as shown in the diagram with USERNAME as the value
    of the root.

    >>> pytunes = make_pytunes('i_love_music')
    >>> print_tree(pytunes)
    i_love_music
      pop
        justin bieber
          single
            what do you mean?
        2024 pop mashup
      trance
        darude
          sandstorm
    """
    #RQ1
    return tree(username, [tree("pop", [tree("justin bieber", [tree("single", [tree("what do you mean?")])]), tree("2024 pop mashup")]), tree("trance", [tree("darude", [tree("sandstorm")])])])

def num_songs(t, n = 0):
    """Return the number of songs in the pyTunes tree, t.

    >>> pytunes = make_pytunes('i_love_music')
    >>> num_songs(pytunes)
    3
    """
    #RQ2 
    if is_leaf(t):
        return 1
    else:
        return sum([n] + [num_songs(x, n) for x in branches(t)])

def add_song(t, song, category):
    """Returns a new tree with SONG added to CATEGORY. Assume the CATEGORY
    already exists.

    >>> indie_tunes = tree('indie_tunes',
    ...                  [tree('indie',
    ...                    [tree('vance joy',
    ...                       [tree('riptide')])])])
    >>> new_indie = add_song(indie_tunes, 'georgia', 'vance joy')
    >>> print_tree(new_indie)
    indie_tunes
      indie
        vance joy
          riptide
          georgia

    """
    #RQ3
    subtrees = [t]
    while True: # Traverse the tree
        for t0 in subtrees:
            if root(t0) == category:
                t0.append(tree(song)) # We found the place we need to add the song
                return t
            for b in branches(t0):
                subtrees.append(b)
        subtrees.pop(0)
        if len(subtrees) == 0:
            print("Could not find category " + category)
            break
    return t

# Tree ADT
def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(root(t), [copy_tree(b) for b in branches(t)])


def delete(t, target):
    """Returns the tree that results from deleting TARGET from t. If TARGET is
    a category, delete everything inside of it.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                                 tree('uptown funk'),
    ...                                 tree('see you again')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    """
    #RQ4
    newtree = tree(root(t))
    subtrees = branches(t)
    parents = [root(t) for _ in subtrees] # Keep track of the node above the current one (duplicates are possible since this is a binary tree)
    while True:
        copySubTrees = [copy_tree(x) for x in subtrees] # Even though copy_tree is marked as testing only, I can't think of another way to do this
        for subtree in copySubTrees:
            if root(subtree) != target:
                newtree = add_song(newtree, root(subtree), parents[0]) # Repurpose add_song to copy data from the old tree to the new tree
                for branch in branches(subtree):
                    subtrees.append(branch)
                    parents.append(root(subtree))
            subtrees.pop(0)
            parents.pop(0)
        if len(subtrees) == 0: # Theres no more data to try and copy over, we are done
            break
    return newtree

import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True) 