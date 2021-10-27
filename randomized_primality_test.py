import doctest
import random

def randomized_primality_test(n):
    """Check if integer ~n~ is prime by leveraging Fermat's Little Theorem and randomization.
    If ~n~ is prime, we know that any integer ~a~ less than ~n~ will be relatively prime to ~n~.
    Thus, per prime number theory, if ~n~ and ~a~ have a gcd(a,n) != 1, ~n~ must be composite.
    However, a GCD of 1 between ~a~ and ~n~ does not guarantee that ~n~ is prime (ex., gcd(9,14)=1).
    Follow-up by testing for primality using FLT. If a**(n-1) != 1 (mod(n)), ~n~ must be composite.
    The algorithm can at best reject ~n~ if it is NOT prime, but cannot definitively identify a prime.
    This is a Monte Carlo class randomized algorithm, since it is correct with high probability
    of at least 50% for non-Carmichael number composites.

    >>> randomized_primality_test(7919)
    '7919 might be prime'
    >>> randomized_primality_test(561)
    '561 might be prime'
    >>> randomized_primality_test(289731)
    '289731 is composite'
    """

    a = random.randint(1, n-1)
    if gcd(a, n) != 1:
        return f"{n} is composite"
    elif a**(n-1) % n != 1:
        return f"{n} is composite"
    else:
        return f"{n} might be prime"

def gcd(a, n):
    """Simple Euclidean algorithm to calculate the GCD of two integers.
    """
    if a == 0:
        return n
    return gcd(n % a, a)


if __name__ == "__main__":
    doctest.testmod()