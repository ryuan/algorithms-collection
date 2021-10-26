import doctest

def insertion_sort(arr):
    """
    Standard insertion sort algorithm exhibiting inefficient O(n**2) running time.

    >>> insertion_sort([4, 2, 5, 1, 8, 9, 7, 4])
    [1, 2, 4, 4, 5, 7, 8, 9]
    >>> insertion_sort([6, 4, 2, 1])
    [1, 2, 4, 6]
    >>> insertion_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    """

    for j in range(1, len(arr)):
        # The element to be sorted at index ~j~ is assigned to ~key~ 
        key = arr[j]
        
        # Trailing pointer ~i~ indicates the element that is compared against ~key~
        # Each loop starts with ~i~ trailing ~j~ by index of 1
        i = j-1
        
        # Keep reducing/moving back trailing pointer ~i~ until it finds a value greater than ~key~
        # Loop invariant necessitates that all elements less than ~key~ are correctly sorted
        # Thus, at the beginning of each ~j~ loop, ~i~ must be the largest value in ~arr[1..j-1]~
        # Loop will keep assigning ~arr[i]~ to ~arr[i+1]~ until it finds sorted position for ~key~
        while i>=0 and arr[i]>key:
            arr[i+1] = arr[i]
            i -= 1
        # ~key~ is assigned to the correct index element in array
        arr[i+1] = key

    return arr


if __name__ == "__main__":
    doctest.testmod()