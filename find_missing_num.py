import doctest

def find_missing_num(arr, p=0, r=None):
    """Given a SORTED array of ~n-1~ elements in the range of 1 to ~n~,
    find the missing element assuming the array has no duplicates.
    Algorithm uses divide and conquer to more efficiently find the missing element.

    >>> find_missing_num([1, 2, 3, 4, 5, 7])
    6
    >>> find_missing_num([1, 2, 3, 5, 6, 7])
    4
    >>> find_missing_num([1, 3, 4, 5, 6, 7])
    2
    >>> find_missing_num([1, 2, 3, 4, 5, 6, 8])
    7
    >>> find_missing_num([1, 2, 3, 4, 5, 7, 8])
    6
    >>> find_missing_num([1, 2, 3, 4, 6, 7, 8])
    5
    >>> find_missing_num([1, 2, 3, 5, 6, 7, 8])
    4
    >>> find_missing_num([1, 2, 3, 5, 6, 7, 8, 9, 10])
    4
    >>> find_missing_num([1, 2, 3, 4, 5, 6])
    7
    >>> find_missing_num([2, 3, 4, 5, 6])
    1
    """

    # Let ~r~ be the largest index in the array being searched
    if r == None:
        r = len(arr) - 1

    # Base case is the smallest index in array whose value is 1 greater than it's sort order,
    # then it signals that the number below it is missing.
    # Otherwise, if the highest indexed number matches its correct sort order value,
    # then it signals that the missing number is actually the largest value possible ~n~.
    if p == r:
        return arr[r] - 1
    elif arr[r] == r + 1:
        return arr[r] + 1

    # For each recursion, calculate the middle expected value within the ~p~ and ~r~ index range
    mid = (p + r)//2

    # Check is ~mid~ index value is actually equal to ~mid~ (note adjustment of 1 for 0-indexing)
    if arr[mid] == mid + 1:
        return find_missing_num(arr, mid+1, r)
    elif arr[mid] > mid + 1:
        return find_missing_num(arr, p, mid)


if __name__ == "__main__":
    doctest.testmod()