import doctest

def knapsack_problem(w_arr, v_arr, W):
    """Another classic algorithm using dynamic programming design.
    The algorithm answers the question: given a list of items with item weight and value,
    what is the max value of item combination that can fit into a knapsack with a weight limit?

    >>> w_arr = [5, 7, 2]
    >>> v_arr = [13, 10, 5]
    >>> W = 10
    >>> knapsack_problem(w_arr, v_arr, W)
    18
    >>> w_arr = [2, 4, 6, 3]
    >>> v_arr = [13, 2, 5, 15]
    >>> W = 15
    >>> knapsack_problem(w_arr, v_arr, W)
    35
    """

    n = len(v_arr)

    # Create an empty value matrix with rows for each item and columns for each weight integer
    # The base case is value of 0 for rows of 0 items and column of 0 weight
    v_matrix = [[0 for j in range(W+1)] for i in range(n+1)]

    # The subproblem is defined as the max value of item combination 
    # considering items 1 to ~i~ for weight capacity up to ~j~
    # Each new item or weight can reuse solutions to previous subproblems to assess maximum value
    for i in range(1, n+1):
        for j in range(1, W+1):
            if j < w_arr[i-1]:
                v_matrix[i][j] = v_matrix[i-1][j]
            else:
                v_matrix[i][j] = max(v_matrix[i-1][j], v_matrix[i-1][j-w_arr[i-1]] + v_arr[i-1])

    return v_matrix[n][W]


if __name__ == "__main__":
    doctest.testmod()