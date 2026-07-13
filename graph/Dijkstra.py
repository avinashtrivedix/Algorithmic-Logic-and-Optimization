# the greedy choisce guarantees that once we pop a node from the heap, we have fouind the absolute shortest path to it.


import heapq
def dijkstra(graph: dict, start: int) -> dict:
    # distances[node] = infinity initially
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # min-heap stores (distance, node)
    pq = [(0,start)]
    while pq:
        current_dist, u = heapq.heappop(pq)

        # Optimization: If we found a shorter path already, skip the stale one.
        if current_dist > distances[u]:
            continue

        for v, weight in graph[u]:
            distance = current_dist + weight
            # Relaxation step
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))

    return distances


if __name__ == "__main__":
    # Test case: Graph as adjacency list {node: [(neighbor, weight), ...]}
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    # Expected:    0->0=0, 0->2=1, 0->1=3 (via 2), 0->3=4 (via 1)
    results = dijkstra(graph, 0)
    print(f"Shortest paths from 0: {results}") 
    assert results[3] == 4, f"Expected 4, got {results[3]}"