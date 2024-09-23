from collections import defaultdict, deque

class ConnectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_connected(self):
        visited = set()
        queue = deque([next(iter(self.graph))])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return len(visited) == len(self.graph)

# Example usage
g = ConnectedGraph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("Graph is connected:" if g.is_connected() else "Graph is not connected")