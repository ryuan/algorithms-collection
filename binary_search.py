import doctest

def binary_search(arr, x, p=0, r=None):
    """A simple, yet extremely fundamental algorithm demonstrating divide and conquer design.
    Requires a sorted array of elements in order to be successful.
    Parameter ~x~ is the search value. ~p~ and ~r~ are beginning and ending search indices, resp.

    >>> binary_search([2, 3, 4, 10, 40], 10)
    3
    >>> binary_search([1, 3, 5, 8, 10, 99, 100], 100)
    6
    >>> binary_search([1, 3, 5, 8, 10, 99, 100], 4)
    '4 not in array'
    """

    if r == None:
        r = len(arr) - 1

    # Base case is when there's no index range to search, meaning ~x~ is not present.
    if p > r:
        return f'{x} not in array'

    # Calculate midpoint ~q~ of subarray as the benchmark
    q = (p + r) // 2

    # If ~x~ is equal to ~q~, then it can only be present in left subarray
    if x == arr[q]:
        return q
    # If ~x~ is smaller than ~q~, then it can only be present in left subarray
    elif x < arr[q]:
        return binary_search(arr, x, p, q-1)
    # If ~x~ is larger than ~q~, then it can only be present in right subarray
    else:
        return binary_search(arr, x, q+1, r)


if __name__ == "__main__":
    doctest.testmod()