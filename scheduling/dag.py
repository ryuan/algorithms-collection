from typing import DefaultDict, Dict, List, Tuple
from operator import itemgetter
from itertools import groupby


class DAG:
    def __init__(self, tasks: Dict[str, int], dependencies: List[Tuple[str, str]]):
        self.tasks = tasks
        self.dependencies = dependencies

        self.vertices = [vertex for vertex in tasks.keys()]
        self.adj = DefaultDict(list)
        for vertex in self.vertices:
            self.adj[vertex]
            for d in self.dependencies:
                if d[0] == vertex:
                    self.adj[vertex].append(d[1])
        
        self.discovery = {vertex: 0 for vertex in tasks.keys()}
        self.finish = {vertex: 0 for vertex in tasks.keys()}
        self.parent = {vertex: None for vertex in tasks.keys()}
        self.color = {vertex: "WHITE" for vertex in tasks.keys()}

        self.time = 0

        self.rev_top_order = []

    def top_order(self):
        return list(reversed(self.rev_top_order))