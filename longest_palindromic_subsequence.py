import doctest

def longest_palindromic_subsequence(string):
    """Computes the length of a longest palindromic subsequence in a string.
    Recall that a palindromic subsequence is a sequence of (not necessarily contiguous)
    characters selected in order such that it reads the same forwards as backwards.
    This is another algorithm designed with dynamic programming.

    >>> longest_palindromic_subsequence("ABCDA")
    3
    >>> longest_palindromic_subsequence("ABCCDA")
    4
    >>> longest_palindromic_subsequence("ABCDCA")
    5
    >>> longest_palindromic_subsequence("AabcBdefCghijkBlmnAo")
    5
    >>> longest_palindromic_subsequence("AabcBdefCCghijkBlmnAo")
    6
    >>> longest_palindromic_subsequence("AabcBdefCghijkClmnoBpqrAst")
    7
    """
    
    n = len(string)

    # Build an ~n~ by ~n~ DP table to store subproblem solutions in
    # The rows and columns in the table correspond to character index in input string ~S~
    m = [[0 for i in range(n)] for j in range(n)]

    # Fill in table with 1 for single character palindromes
    for i in range(n):
        m[i][i] = 1

    # Loop through different successively larger chain lengths ~l~ to fill DP table
    # If the ends of the chain at ~i~ and ~j~ match, add 2 to larger of two 1-index smaller subsequence solutions
    # If the ends do not match, just fill with larger of two 1-index smaller subsequence solutions
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if string[i] == string[j] and l == 2: #if chain length is two, just fill with 2
                m[i][j] = 2
            elif string[i] == string[j]:
                m[i][j] = 2 + max(m[i][j-1], m[i-1][j])
            else:
                m[i][j] = max(m[i][j-1], m[i+1][j])

    return m[0][n-1]    #return the corner solution in the top right (i.e., full length LPS)


if __name__ == "__main__":
    doctest.testmod()