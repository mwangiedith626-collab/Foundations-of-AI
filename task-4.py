from collections import deque

# --- Breadth First Search (BFS) ---
def bfs(graph, start, goal):
    """
    Perform Breadth First Search.
    Returns the path from start to goal.
    """
    visited = set()
    queue = deque([[start]])   # queue stores paths

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path   # found goal

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None


# --- Depth First Search (DFS) ---
def dfs(graph, start, goal):
    """
    Perform Depth First Search.
    Returns the path from start to goal.
    """
    visited = set()
    stack = [[start]]   # stack stores paths

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path   # found goal

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return None

# --- Example Graph ---
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# --- Run Searches ---
print("BFS path from A to F:", bfs(graph, 'A', 'F'))
print("DFS path from A to F:", dfs(graph, 'A', 'F'))
