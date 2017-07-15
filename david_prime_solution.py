import math
import numpy as np 
import re
from math import sqrt

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1

def print_list(items, cols=2):
    """ Print List as Matrix
    Prints a list in columns, given column num
    """
    # use numpy.  Format lists to tab after each item
    np.set_printoptions(formatter={'all':lambda x: str(-x)+'\t'})
    # turn array into numpy one
    arr = np.array(items)
    # split into columns and print
    for x in np.array_split(arr, int(cols)):
        print x

def checkIntValue(question):
    '''Works fine for check if an **input** is
   a positive Integer AND in a specific range'''
    maxValue = 20
    intTarget = 0
    while intTarget < 1 or intTarget > maxValue:
        try:
            intTarget = int(raw_input(question))
        except ValueError:
            continue
        else:
            break

    return (intTarget)

def get_coords():
    """ Get Coords from User
    Presents question for user input, validates, and returns
    """
    coords = (checkIntValue("How many columns would you like? "), checkIntValue("How many primes would you like generated? "))

    return coords

if __name__ == "__main__":
    # get (columns, number of primes) from user #
    columns, num_primes = get_coords()
    # generate primes #
    print "Generating primes..."
    primes = []
    prime_gen = gen_primes()
    for _ in range(num_primes):
        primes.append(prime_gen.next())
    # print 'er out #
    print_list(primes, columns)