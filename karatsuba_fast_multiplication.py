import doctest
from math import ceil, floor

def karatsuba_fast_multiplication(x, y):
    """
    The fast multiplication algorithm developed by Karatsuba as a 23-year old student in 1960
    to prove that multiplication can be achieved in less than O(n**2) time.
    This is a clever adaptation of the standard divide and conquer multiplication algorithm
    and is able to multiply two *n*-digit integers in O(n**lg(3)) time.
    
    >>> karatsuba_fast_multiplication(23, 14)
    322
    >>> karatsuba_fast_multiplication(256, 133)
    34048
    >>> karatsuba_fast_multiplication(12345, 6789)
    83810205
    >>> karatsuba_fast_multiplication(377, 37)
    13949
    """

    # Base case is both x and y being single digits, in which case just return their product
    if x< 10 and y < 10:
        return x * y

    # Determine the longest digit length between x and y
    size = max(len(str(x)), len(str(y)))

    # Split x and y, ensuring that the right half always gets the extra digit in case *n* is odd
    n = ceil(size // 2)
    power = 10 ** n
    x_0 = x // power
    x_1 = x % power
    y_0 = y // power
    y_1 = y % power

    # Recursively call function until base case is reached, then multiply back up
    # Note that 'z_1' reuses results from 'z_0' and 'z_2', which reduces number of product operations
    # In other words, '(x_0+x_1)*(y_0+y_1) - z_0 - z_2' is equal to 'x_0*y_1 + x_1*y_0'
    # By multiplying once instead of twice, the algo is able to greatly decrease calculation speed
    z_0 = karatsuba_fast_multiplication(x_0, y_0)
    z_2 = karatsuba_fast_multiplication(x_1, y_1)
    z_1 = karatsuba_fast_multiplication(x_0 + x_1, y_0 + y_1) - z_0 - z_2

    # Return the result of the product
    return int(10 ** (2 * n) * z_0 + (10 ** n) * z_1 + z_2)


if __name__ == "__main__":
    doctest.testmod()