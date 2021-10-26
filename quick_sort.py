import doctest

def quick_sort(arr, p=0, r=None):
    """
    Implementation of the standard quick sort algorithm using divide and conquer.
    Goal is to achive merge sort's O(n*log(n)) run time and insertion sort's in-place sorting.
    Without randomization, quick sort will deterministically require O(n**2) on pre-sorted input.

    >>> quick_sort([4, 2, 5, 1, 8, 9, 7, 4])
    [1, 2, 4, 4, 5, 7, 8, 9]
    >>> quick_sort([6, 4, 2, 1])
    [1, 2, 4, 6]
    >>> quick_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    """

    # Allow passing of array without additional arguments in initial method call
    if r == None:
        r = len(arr) - 1

    # Base case is when indices for partitioning match, indicating lone or no element
    # Otherwise, recursively partition array into two segments around pivot value
    # Note that the pivot value is ignored after parition since it is in the final sorted index
    if r > p:
        pivot = partition(arr, p, r)
        quick_sort(arr, p, pivot-1)
        quick_sort(arr, pivot+1, r)

        return arr


def partition(arr, p, r):
    """
    Sorts array into two partitions: left partition's values <= pivot value < right parition's values
    """

    # Always define pivot value as the ~r~ indexed element
    pivot = arr[r]
    # ~i~ pointer marks boundary for partitioned elements that are <= to pivot's value 
    i = p - 1

    # ~j~ pointer marks boundary for elements that still remain to be partitioned
    # [elements less than or equal to pivot] ~i~ [elements greater than pivot] ~j~ [unknown] ~pivot~
    for j in range(p, r):
        # If element at index ~j~ is less than or equal to pivot, move it within ~i~ boundary
        # The element at ~i+1~ index swaps places with it since it's between ~i~ and ~j~
        # and thus is already partitioned and guaranteed to be larger than the pivot value
        # If ~i~ and ~j~ are pointing at the same index, than they essentially just increment together
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Once everything is partitioned, swap and move pivot to its final sorted index
    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i + 1


if __name__ == "__main__":
    doctest.testmod()