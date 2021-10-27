import doctest

def fast_fibonacci(n):
    """A basic algorithm to demonstrate the advantage of dynamic programming.
    Compared to the naive Fibonacci algorithm, this algorithm reduces the time complexity
    from exponential down to polynomial/linear as a function of ~n~.  

    >>> fast_fibonacci(9)
    34
    >>> fast_fibonacci(20)
    6765
    """

    if n == 0:
        return 0
    
    # Base case for Fibonacci requires the first two numbers in the sequence
    arr = []
    arr.append(0)
    arr.append(1)
    # Use the array to store preceeding solutions to avoid repeating recursive calls 
    for i in range(2, n+1):
        arr.append(arr[i-1] + arr[i-2])

    return arr[n]


if __name__ == "__main__":
    doctest.testmod()