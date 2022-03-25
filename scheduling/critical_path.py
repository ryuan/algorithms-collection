from typing import Dict, List, Tuple
from dag import DAG


def critical_path(tasks: Dict[str, int], dependencies: List[Tuple[str, str]]) -> Tuple[int, List[str]]:
    """
    Computes a critical path for the provided tasks and dependencies
    :param tasks: Dictionary of (task, duration) pairs. Duration is a positive number of days.
    :param dependencies: List of (task1, task2) pairs, where task1 must be completed before task2.
    :return length, path: Length is the total length of a critical path in days.
    Path is a list of tasks which belong to some critical path, in order from start to finish.
    >>> tasks = {"A": 6, "B": 2, "C": 4, "D": 3, "E": 11}
    >>> dependencies = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
    >>> critical_path(tasks, dependencies)
    (13, ['A', 'C', 'D'])
    >>> tasks["E"] = 15  # Task E now takes 15 days
    >>> critical_path(tasks, dependencies)
    (15, ['E'])
    """

    g = DAG(tasks, dependencies)
    dfs(g)
    
    max_duration = [(None,-1) for i in range(len(tasks))]
    v_i = {vertex: i for i, vertex in enumerate(g.top_order())}

    for u in g.top_order():
        if g.parent[u] == None:
            max_duration[v_i[u]] = (None, tasks[u])
        for v in g.adj[u]:
            if max_duration[v_i[v]][1] < max_duration[v_i[u]][1] + tasks[v]:
                max_duration[v_i[v]] = (u, max_duration[v_i[u]][1] + tasks[v])


    max_length = 0
    max_i = 0
    for i, tup in enumerate(max_duration):
        if tup[1] > max_length:
            max_length = tup[1]
            max_i = i

    path = []
    if max_duration[max_i][0] == None:
        path.append(g.top_order()[max_i])
    else:
        while max_duration[max_i][0] is not None:
            path.append(g.top_order()[max_i])
            max_i = v_i[max_duration[max_i][0]]
            if max_duration[max_i][0] == None:
                path.append(g.top_order()[max_i])
    path.reverse()
    
    return (max_length, path)


def dfs(g: DAG):
    for u in g.vertices:
        if g.color[u] == "WHITE":
            dfs_visit(g, u)


def dfs_visit(g: DAG, u):
    g.time += 1
    g.discovery[u] = g.time
    g.color[u] = "GRAY"

    for v in g.adj[u]:
        if g.color[v] == "WHITE":
            g.parent[v] = u
            dfs_visit(g, v)
    
    g.color[u] = "BLACK"
    g.rev_top_order.append(u)
    g.time += 1
    g.finish[u] = g.time


if __name__ == "__main__":
    import doctest
    doctest.testmod()