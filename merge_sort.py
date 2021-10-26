import doctest

def merge_sort(arr):
    """
    Application of classic divide and conquer algorithm design technique.
    Per the master theorem, the merge sort algorithm exhibits O(n*log(n)) time complexity.
    However, it does not sort in place and is therefore inferior to quick sort.
    >>> merge_sort([4, 2, 5, 1, 8, 9, 7, 4])
    [1, 2, 4, 4, 5, 7, 8, 9]
    >>> merge_sort([6, 4, 2, 1])
    [1, 2, 4, 6]
    >>> merge_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    """

    # If the array contains more than one element, sort it.
    # Otherwise, it is already trivially sorted as an array of one or no element (i.e., base case).
    if len(arr) > 1:
        # Calculate the middle index of the array, then split the array into left and right halves.
        # Recursively call merge_sort() on each half, returning sorted array
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        # Initialize the pointer variables:
        # *i* for left array, *j* for right array, and *k* for merged array
        i = j = k = 0

        # Append sentinel value of infinity to left and right arrays
        left.append(float('inf'))
        right.append(float('inf'))

        # Loops through left and right arrays, copying the smaller of 2 values into merged array
        # If either *i* or *j* reach the sentinel, copy remainder of other array to merged array  
        for k in range(len(left)+len(right)-2):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

    return arr

if __name__ == "__main__":
    doctest.testmod()