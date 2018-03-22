from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    #Split string a and b into 2 sets for comparison
    x = set(a.split("\n"))
    y = set(b.split("\n"))

    if (x == set() or y == set()):
        return("")

    else:
        return(x.intersection(y))

def sentences(a, b):
    """Return sentences in both a and b"""

    # Store sets of a and b into x and y
    x = set(sent_tokenize(a))
    y = set(sent_tokenize(b))

    #return the intersection of 2 sets
    return (x.intersection(y))


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    length_a = len(a)
    length_b = len(b)

    #iterate over a and b strings up to end of strings, get substring of size n and store in x and y respectively
    x = set(a[i:i+n] for i in range(length_a - (n-1)))
    y = set(b[i:i+n] for i in range(length_b - (n-1)))

    #return the intersect of x and y
    return (x.intersection(y))
