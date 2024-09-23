from collections import deque

# Using deque as a queue
queue = deque()

# Adding elements (enqueue)
queue.append(1)
queue.append(2)
queue.append(3)

# Removing elements (dequeue)
print(queue.popleft())  # Output: 1
print(queue.popleft())  # Output: 2

#----------------------------------------------------------------------------
from collections import deque

def bfs_shortest_path(graph, start, end):
    # Initialize the queue with the start node and the path taken so far
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        # Dequeue the next node and the path taken to reach it
        current_node, path = queue.popleft()

        # If we have reached the end node, return the path
        if current_node == end:
            return path

        # Mark the current node as visited
        visited.add(current_node)

        # Enqueue all unvisited neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    # If there is no path from start to end
    return None

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
end_node = 'E'
shortest_path = bfs_shortest_path(graph, start_node, end_node)
print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")


print(hash("hello"))  # Output: A hash value (e.g., 532575546325)
print(hash(12345))    # Output: A hash value (e.g., 12345)
