import doctest

def count_inversions(arr, p=0, r=None):
    """
    Counts the number of inversions in a list.
    Inversion is defined as a pair of indices (i, j) such that i < j and arr[i] > arr[j].
    The algorithm is designed as a variant of merge sort that counts the difference in
    indices whenever an element from right array needs to sorted earlier than elements in left. 

    >>> count_inversions([1, 4, 2, 3])
    2
    >>> count_inversions([1, 2, 3, 4])
    0
    >>> count_inversions([3, 3, 2, 1])
    5
    >>> count_inversions([2, 4, 1, 3, 5])
    3
    >>> count_inversions([5, 6, 7, 8, 1, 2, 3, 4])
    16
    >>> count_inversions([4, 3, 2, 1])
    6
    """

    # Allow passing of array without additional arguments in initial method call
    if r == None:
        r = len(arr) - 1

    inversion_count = 0

    if p < r:
        q = (p + r) // 2
        inversion_count += count_inversions(arr, p, q)
        inversion_count += count_inversions(arr, q + 1, r)
        inversion_count += merge(arr, p, q, r)

    return inversion_count

def merge(arr, p, q, r):
    inversion_count = 0
    n1 = q - p + 1
    n2 = r - q
 
    left = [0] * (n1)
    right = [0] * (n2)
 
    # Copy data to left and right subarrays from main array
    for i in range(0, n1):
        left[i] = arr[p + i]
 
    for j in range(0, n2):
        right[j] = arr[q + 1 + j]

    # Append sentinel value of infinity to left and right arrays
    left.append(float('inf'))
    right.append(float('inf'))
 
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = p     # Initial index of merged subarray
 
    # Sort and merge the left and right subarrays back to the main array
    # Increase inversion counter if an element in the left is greater than an element in the right
    # If either ~i~ or ~j~ reach the sentinel, copy remainder of other array to merged array
    for _ in range(len(left)+len(right)-2):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            # Increase counter by the length from the current index to the middle of the main array
            inversion_count += n1 - i
            j += 1
        k += 1

    return inversion_count

if __name__ == "__main__":
    doctest.testmod()
