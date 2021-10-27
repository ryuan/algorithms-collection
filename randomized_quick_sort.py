import doctest
import random

def randomized_quick_sort(arr, p=0, r=None):
    """
    A variant of the standard quick sort algorithm with randomized pivot selection.
    Randomization enables the algorithm to achieve in-place sorting at O(n*log(n)) 'expected' time.
    This is an example of a Las Vegas algorithm since for a given input on different executions,
    randomized quick sort produces the same output with potentially different number of steps.
    Though it treats for pre-sorted input, it still suffers if given non-distinct element arrays.

    >>> randomized_quick_sort([4, 2, 5, 1, 8, 9, 7, 4])
    [1, 2, 4, 4, 5, 7, 8, 9]
    >>> randomized_quick_sort([6, 4, 2, 1])
    [1, 2, 4, 6]
    >>> randomized_quick_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    """

    # Allow passing of array without additional arguments in initial method call
    if r == None:
        r = len(arr) - 1

    # Base case is when indices for partitioning match, indicating lone or no element
    # Otherwise, recursively partition array into two segments around randomized pivot value
    # Note that the pivot value is ignored after parition since it is in the final sorted index
    if r > p:
        x = random.randint(p, r)
        arr[x], arr[r] = arr[r], arr[x]
        pivot = partition(arr, p, r)
        randomized_quick_sort(arr, p, pivot-1)
        randomized_quick_sort(arr, pivot+1, r)

        return arr


def partition(arr, p, r):
    """
    Sorts array into two partitions:
    left partition contains values <= to pivot | right partition contains values > pivot
    """

    # ~r~ indexed element has been randomized
    pivot = arr[r]
    # ~i~ pointer marks boundary for partitioned elements that are <= to pivot's value 
    i = p - 1

    # ~j~ pointer marks boundary for elements that still remain to be partitioned
    # [values <= to pivot] ~i~ | [values > pivot] ~j~ | [unknown] | ~pivot~
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