import doctest

def lcs(x, y):
    """Given two character sequences ~x~ and ~y~, find the longest subsequence length.
    The algorithm takes O(mn) time assuming ~x~ and ~y~ have ~m~ and ~n~ lengths, respectively.
    Using DP, subproblems are solved once, stored, and reused to solve the original problem.

    >>> x = "abcbdab"
    >>> y = "bdcaba"
    >>> lcs(x, y)
    4
    """

    x = list(x)
    y = list(y)
    m = len(x)
    n = len(y)

    # Create a DP table to store LCS given any ~i~ and ~j~ lengths subsequences of ~x~ and ~y~
    lcs_table = [[0 for j in range(0, n+1)] for i in range(0, m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                lcs_table[i][j] = lcs_table[i-1][j-1] + 1
            elif lcs_table[i-1][j] >= lcs_table[i][j-1]:
                lcs_table[i][j] = lcs_table[i-1][j]
            else:
                lcs_table[i][j] = lcs_table[i][j-1]

    return lcs_table[m][n]


if __name__ == "__main__":
    doctest.testmod()