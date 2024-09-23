from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Initialize an empty adjacency list

    def add_edge(self, u, v):
        self.graph[u].append(v)  # Add an edge from vertex u to vertex v

    def bfs(self, start):
        visited = set()  # Set to keep track of visited vertices
        queue = deque([start])  # Initialize a queue with the start vertex

        while queue:
            vertex = queue.popleft()  # Dequeue a vertex from the queue
            if vertex not in visited:
                print(vertex, end=' ')  # Print the vertex
                visited.add(vertex)  # Mark the vertex as visited
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)  # Enqueue non-visited neighbors

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Breadth-First Search starting from vertex 2:")
g.bfs(2)