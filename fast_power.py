import doctest

def fast_power(a, n):
    """Greatly reduce the number of multiplications involved in computing
    large powers of a number by explotiing binary exponentiation.
    Achieves O(lg(n)) time complexity, compared to O(n) for the naive method.

    >>> fast_power(3, 11)
    177147
    >>> fast_power(2, 8)
    256
    """

    # Base case is a number raised to power of 1, so return the number
    if n == 1:
        return a
    else:
        # Recursively call fast_power() to perform repeated squaring from base case up
        x = fast_power(a, n // 2)
        if n % 2 == 0:
            return x * x
        else:
            # If ~n~ is odd, the original call will do the final multiplication to accomodate
            return x * x * a


if __name__ == "__main__":
    doctest.testmod()