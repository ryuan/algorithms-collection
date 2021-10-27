import doctest

def matrix_chain_order(arr):
    """More advanced implementation of dynamic programming to identify
    optimal parenthesization for minimal matrix chain multiplication operations.
    Though time complexity is high at O(n**3), it is still polynomial.
    The input is an array of number of rows and columns for some valid matrix chain.

    >>> matrix_chain_order([1, 1000, 1, 1000])
    (2000, 1)
    """

    n = len(arr)
    # Initialize two DP tables:
    # ~m_table~ to store subproblem solutions for number of multiplications
    # ~s_table~ to store subproblem solutions for split points
    # Note that with python implementation, split is 0-indexed, so 1 means split at matrix 2
    m_table = [[0 for i in range(0, n-1)] for j in range(0, n-1)]
    s_table = [[0 for i in range(0, n-1)] for j in range(0, n-2)]

    # ~l~ loops through chain length possibilities
    for l in range(2, n):
        # ~i~ loops through chain's left starting index
        for i in range(0, n-l):
            # ~j~ is just the chain's right ending index given ~i~ and chain length ~l~
            j = i + l - 1
            # Insert a sentinel value to ensure storage of first iteration multiplication volume
            m_table[i][j] = float('inf')
            for k in range(i, j):
                # ~q~ is the subproblem solved by recurrence referencing previously solved subproblems
                # It calculates the number of scalar multiplcations needed to compute the chain,
                # storing the minimum number of operation for the chain looping through pivot points
                q = m_table[i][k] + m_table[k+1][j] + arr[i]*arr[k]*arr[j]
                if q < m_table[i][j]:
                    m_table[i][j] = q
                    s_table[i][j] = k

    return m_table[0][n-2], s_table[0][n-2]


if __name__ == "__main__":
    doctest.testmod()