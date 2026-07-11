# given an unweighed graph represents as an adjacency list and a startinf node, find the shortet distance (number of edges ) to all other nodes
# the strategy - breadth first search (bfs)
# level by level exploratio : Unlike DFS (which dives deep), BFS explores all neighbors of the start node first, then all neighbors of those neighbors.
# the queue : you store the node and its current distance(node, distance)
# the seen set: To prevent infinite loops, you must track which nodes you have already visited

from collections import deque
def shortest_path(graph: dict, start:int) -> dict:
    """
    finds the shortest path in an unweighed graph using bfs
    time complexity : O(V+E) - we visit each vertex and edge once
    Space Complexity : O(V) - we store the que and the seen set
    """

    distances = {node: -1 for node in graph}
    distances[start] = 0
    queue = deque([start])

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if distances[v] == -1: # If not visited 
                distances[v] = distances[u] + 1
                queue.append(v)

    return distances

if __name__ == "__main__":
    graph = {
        0: [1,2],
        1: [0, 3], 
        2: [0, 4], 
        3: [1], 
        4: [2]
    }
    print(f"Shortest paths: {shortest_path(graph, 0)}") # Expected: {0:0, 1:1, 2:1, 3:2, 4:2}







