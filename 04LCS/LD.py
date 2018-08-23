import time
from functools import wraps
import cProfile
import numpy
import Levenshtein

def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s: %s seconds" % (function.__name__, str(t1 - t0)) )
        return result
    return function_timer

def levenshtein1(source, target):
    if len(source) < len(target):
        return levenshtein1(target, source)
    if len(target) == 0:
        return len(source)
    # We call tuple() to force strings to be used as sequences
    # ('c', 'a', 't', 's') - numpy uses them as values by default.
    source = numpy.array(tuple(source))
    target = numpy.array(tuple(target))
    # We use a dynamic programming algorithm, but with the added optimization that we only
    #  need the last two rows of the matrix.
    previous_row = numpy.arange(target.size + 1)
    for s in source:
        # Insertion (target grows longer than source):
        current_row = previous_row + 1
        # Substitution or matching:
        # Target and source items are aligned, and either
        # are different (cost of 1), or are the same (cost of 0).
        current_row[1:] = numpy.minimum(
            current_row[1:],
            numpy.add(previous_row[:-1], target != s))
        # Deletion (target grows shorter than source):
        current_row[1:] = numpy.minimum(
            current_row[1:],
            current_row[0:-1] + 1)
        previous_row = current_row
    return previous_row[-1]

def levenshtein2(s1, s2):
    if len(s1) < len(s2):
        return levenshtein2(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def levenshtein3(s, t):
    ''' From Wikipedia article; Iterative with two matrix rows. '''
    if s == t:
        return 0
    elif len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]
    return v1[len(t)]

@fn_timer
def calllevenshtein1(s, t, n):
    for i in range(n):
        t1 = levenshtein1(s, t)
@fn_timer
def calllevenshtein2(s, t, n):
    for i in range(n):
        t2 = levenshtein2(s, t)
        print(t2)
@fn_timer
def calllevenshtein3(s, t, n):
    for i in range(n):
        levenshtein3(s, t)
@fn_timer
def calllevenshtein4(s, t, n):
    for i in range(n):
        Levenshtein.distance(s, t)

if __name__ == "__main__":
    n = 1
    a = 'abddcdefdgbd22svb'
    b = 'bcdefg34rdyvdfsd'
    calllevenshtein1(a, b, n)
    calllevenshtein2(a, b, n)
    calllevenshtein3(a, b, n)
    calllevenshtein4(a, b, n)
