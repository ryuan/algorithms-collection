import doctest

def lis(arr):
    """Given an unsorted array, find the longest subsequence of elements in sorted order.
    Algorithm leverages dynamic programing design to avoid repetitive recursive calls.

    >>> lis([11, 14, 13, 7, 8, 15])
    3
    >>> lis([10, 22, 9, 33, 21, 50, 41, 60, 80])
    6
    """

    n = len(arr)
    # Create DP array to store the LIS up to ~x[i]~ for all elements
    lis_array = [1 for i in range(0, n)]
    
    # Solve each subproblem by comparing each ~i~ value to all preceeding values ~j~
    # Obviously, consider the LIS at ~j~ only if the element ~x[j]~ is less than ~x[i]
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis_array[i] < lis_array[j] + 1:
                lis_array[i] = lis_array[j] + 1

    return max(lis_array)


if __name__ == "__main__":
    doctest.testmod()