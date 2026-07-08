"""
some details about the grapghs first
A graph is defined as a pair of (V,E), where :
V : vertices/ Nodes - the object or 'points' in your graph
E : Edges/connections -  the relationships between the vertices 

Directionality -  undirected vs directed grapghs
undirected graphs : Edges have no orientation
directed grapgh (digrphs) : Edges have a direction

Grapgh desity :
sparse ghrapgh :  has few edges compared to the numbers of verites |E|~~|V|
dese grapgh : has many edges compare to the no. of vertices. |E| ~~ |V|^2
why this matters: the choise between an adjacency matrix and the adgacency list for storage depends on the desity

storage Structures
Adjacency Matrix : A 2d array where matrix[i][j] == 1 if an edge exists
pro - fast edge lookups
cons - huge memory waste for sparce graphs (O(V^2))
Adjacency List :  An array (or hashmap) of lists where list[i] contains all neighbors of bertex i
pro - very memory efficient for sparce graphs O(V + E)
con - SLower edge lookups

Important graph properties
degree :  the Number of edges connected to a vertex
path : A sequence of vertices connected by edges.
cycle : A path that starts and ends at the same vertex. 
connected component : A subset of vertices where every veriteces is reachable from every other vertices in that subset.

Traversal differnces 
DFS -  explores as far as possible along each branch before backtracking .
    it uses stack (or recursion) . excellent for puzzles , pathfinding in mazes and cycle detection 
BFS -  explores neighbor nodes first, before moving to the next level neighbors. 
    It uses queue . excellent for finding the shortest path in an unweighed graph

"""

# the problem -  there are numCourses courses labeled from 0 to cumCoursees-1. you are given an array prerequisites
#  where prerequisites[i] = [ai, bi] indicates you have to take, bi before course ai .
#  return true is you can finish all the courses otherwise return false.

# strateygy - cycle detection (kahn's Algorithm)
# this is a directed graph the only way you cant finish courses if there is a cycle (eg. A requires B, B requires A)
# In-degree :  track how many prerequisite courses each courses have.
# Qeue : start with course, decrement thay an in_degree f 0(no prerequisites).
# process : "Complete" a course by removing decrement the in-dgree of its neighbors, and add any new courses that hit in_degree == 0 to the queue.
# verify: if the number of completed course equqls numCourses, you win. 

from collections import deque, defaultdict
# defaultdict - (a a dictionary subclass) its primary purpose is to provide a default value for the key that does not exist, removing the need fot manual boiler checks and initializations.
# boilerplate - refers to the sections of code that you must write repeatedly in multiple places with little or no modification to aciece standard tasks. it is often called code because 

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    check if all courses can be completed using kahn's Algithm
    Time Complexity : O(V+E) - we visit each vertex and edge once
    Space Complexity : O(V+E) - we store the graph and the in-degree counts
    """

    adj = defaultdict(list)
    in_degree = [0] * num_courses

    # Build Graph
    for dest, src in prerequisites:
        adj[src] .append(dest)
        in_degree[dest] += 1

    # queue for courses with no prerequisites
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    completed = 0

    while queue:
        u = queue.popleft()
        completed += 1

        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return completed == num_courses

if __name__ == "__main__":
    print(can_finish(2, [[1, 0]])) # Expected: True