#the heap is the to-do list , it dynamically holds the nodes your are planning to visit next, sorted by who is the cheapest to reach.

# dijkstra is your greedy accountant. 
# preparation (Adjacency list): COnvert the input time into a a dictionary: ADJ = {u: [(v, time),...],... }
# Tracking (Distances) : Create a distance dictionary to keep track of the best time found so far, initialized to infinity.
# the queue: (heap) : start with,heap  = [(0,k)] (time 0, starting node k)
# the loop - 
# pop the node with the smallest time from the heap.
# look at its neighbors in you adj list.
# if new_time (current time + edge weight ) is better than you best recordm update the distance and push (new time, neighbor) to the heap

from collections import defaultdict
import heapq


def networkDelayTime(times, n, k):
    #build the adjacency list(your map)
    adj = defaultdict(list)
    for u,v,w in times:
        adj[u].append((v,w))


    # tracking the fastest time (your accountant book)
    # Initialize all nodes (1 to n) with infinity
    distances = {i: float('inf') for i in range(1, n+1)}
    distances[k] = 0 # starting node takes 0 time


    # the priority queue (to-do list)
    # heap stores (current_time, current_node)

    heap = [(0,k)]

    while heap:
        current_time, u = heapq.heappop(heap)

        # if we already found a faster way to u, ignore this old data
        if current_time > distances[u]:
            continue
        
        # look at neighbors of u
        for v, w in adj[u]:
            new_time  = current_time + w
            # only update if we found a shorter path to v
            if new_time < distances[v]:
                distances[v] = new_time
                heapq.heappush(heap, (new_time, v))

    # final check: did we reach all nodes? If any node is still at infinity, return -1
    result = max(distances.values())
    return result if result < float('inf') else -1

if __name__ == "__main__":
    # Test Case: Signal starts at node 2. 
    # Cable 2->1 (time 1), 2->3 (time 1), 3->4 (time 1)
    # The signal should reach node 4 in 2ms.
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    
    result = networkDelayTime(times, n, k)
    print(f"Shortest time for signal to reach all nodes: {result}")
    
    # Verification
    assert result == 2, f"Expected 2, but got {result}"
    print("Success: Dijkstra implementation verified.")