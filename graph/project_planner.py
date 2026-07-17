# some projects have prerequisites. determine ifi it is possible to finish all projects
# kahns Algorithm - Popular BReadth first search method (BFS) method used to find a topological orderingof directed acyclic ordering. of a directed Acyclic Graph (DAG).
# It operates by repeatedtly finding nodes finding nodes with no incoming dependencies.  (indegree of 0), adding them to the sorted sequence , and removing them form the graph
# count the indegree : Count the number of incoming edges to every node in the graph.
# initialize the queue:  find all the nodes with indegree of 0 , push them into queue.
# process the queue: 
from collections import deque, defaultdict
def project_planner(num_courses: int, prerequisites: list[list[int]])-> bool:
    #initialize the adjacency list and an in-degree count
    adj = defaultdict(list)
    in_degree = [0] * num_courses

    for dest, src in prerequisites:
        adj[src].append(dest)
        in_degree[dest] += 1

    # add all the free project courses (in -degree 0) to the queue
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])

    # process the queue
    processed_count = 0
    while queue:
        curr = queue.popleft()
        processed_count += 1

        for neighbors in adj[curr]:
            in_degree[neighbors] -= 1
            if in_degree[neighbors] == 0:
                queue.append(neighbors)

    return processed_count == num_courses

if __name__ == "__main__":
    # Test Case 1: Possible
    # 0 -> 1
    assert project_planner(2, [[1, 0]]) == True, "Test 1 Failed"
    
    # Test Case 2: Impossible (Cycle)
    # 0 -> 1 -> 0
    assert project_planner(2, [[1, 0], [0, 1]]) == False, "Test 2 Failed"
    
    # Test Case 3: Complex
    # 0 -> 2, 1 -> 2
    assert project_planner(3, [[2, 0], [2, 1]]) == True, "Test 3 Failed"
    
    print("All test cases passed. Kahn's Algorithm verified.")
