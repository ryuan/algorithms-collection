import doctest
import random

def tripartite_rqs(arr, p=0, r=None):
    """A variant of the randomized quick sort algorithm that sorts across three partitions.
    The additional partition is a middle partition consisting of value equal to the pivot value.
    It is able to sort in-place both pre-sorted and non-distinct inputs at O(n*log(n)) 'expected' time.
    This is a Las Vegas randomized algorithm, since it is guaranteed to produce the same output
    for identical inputs, though with potentially different number of computations.

    >>> tripartite_rqs([4, 2, 5, 1, 8, 9, 7, 4])
    [1, 2, 4, 4, 5, 7, 8, 9]
    >>> tripartite_rqs([6, 4, 2, 1])
    [1, 2, 4, 6]
    >>> tripartite_rqs([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> tripartite_rqs([2, 4, 3, 5, 5, 1, 7, 5, 5])
    [1, 2, 3, 4, 5, 5, 5, 5, 7]
    """

    # Allow passing of array without additional arguments in initial method call
    if r == None:
        r = len(arr) - 1

    # Base case is when indices for partitioning match, indicating lone or no element
    # Otherwise, recursively partition array into three blocks around randomized pivot value
    # Uses a tuple to mark the index boundaries for values less than, equal to, and greater than pivot 
    # The middle partition is excluded in recursive calls since they are in final sorted order
    if r > p:
        x = random.randint(p, r)
        arr[x], arr[r] = arr[r], arr[x]
        pivot_tuple = three_way_partition(arr, p, r)
        tripartite_rqs(arr, p, pivot_tuple[0]-1)
        tripartite_rqs(arr, pivot_tuple[1]+1, r)

        return arr


def three_way_partition(arr, p, r):
    """ Sorts array into three partitions:
    left has values < to pivot | middle has values == pivot | right has values > pivot

    >>> three_way_partition([20, 4, 13, 7, 20], 0, 4)
    (3, 4)
    >>> three_way_partition([8, 1, 5, 5, 9], 0, 4)
    (4, 4)
    >>> three_way_partition([2, 4, 3, 5, 5, 1, 7, 5, 5], 0, 8)
    (4, 7)
    """

    # ~r~ indexed element has been randomized
    pivot = arr[r]
    # ~i~ pointer marks boundary for partitioned elements that are less than pivot's value 
    i = p - 1
    # ~k~ pointer marks boundary for partitioned elements that are equal to pivot's value
    k = p - 1

    # ~j~ pointer marks boundary for elements that still remain to be partitioned
    # [values <= to pivot] ~i~ | [values = to pivot] ~k~ | [values > pivot] ~j~ | [unknown] | ~pivot~
    for j in range(p, r):
        # If element at index ~j~ is equal to ~pivot~, move it within ~k~ boundary
        # The element at ~k+1~ index swaps places with it since it's between ~k~ and ~j~
        # and thus is already partitioned and guaranteed to be larger than the pivot value
        # If ~k+1~ and ~j~ are pointing at the same index, than they essentially just increment together
        if arr[j] == pivot:
            k += 1
            arr[k], arr[j] = arr[j], arr[k]
        # If element at index ~j~ is less than ~pivot~, move it within ~i~ boundary
        # First swap ~arr[k+1]~ with ~arr[j]~ since ~arr[k+1] > pivot > arr[j] > arr[i]~ if ~k+1 != j~
        # If ~k+1~ and ~j~ are pointing at the same index, than they just increment together
        # Now swap ~arr[i+1]~ with ~arr[k]~ since ~arr[k]~ now must contain the element to be sorted
        # and ~arr[i+1]~ must either be equal to ~pivot~ since it's between ~i~ and ~k~
        # or ~arr[i+1] == arr[k] == arr[j]~ if ~k == i~ at the beginning of the iteration
        elif arr[j] < pivot:
            k += 1
            arr[k], arr[j] = arr[j], arr[k]
            i += 1
            arr[i], arr[k] = arr[k], arr[i]

    # Once everything is partitioned, swap and move pivot to its final sorted index
    arr[k+1], arr[r] = arr[r], arr[k+1]

    return (i+1, k+1)


if __name__ == "__main__":
    doctest.testmod()