# The story: 
# There are a total of (numCourses) courses you have to take, labeled from 0 to numCourses - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take corse 1. 
# Which is expressed as a pair: [0,1] 
# Return true if you can finish all courses. Otherwise, return False.


# this is classinc Directed gragh cycle detection problem.
# If there is a cycle in the prerequite dependencies
# it is not possible to finish all courses.

# Build an Adjacency List mapping each course to it's lsit of prerequisites. 
# Uses a DFS traversal with a 3 state visited map visited dictionary or array.

# 0 or False: unvisited
# 1 or True: visited 


# what we need -
# Adjacency List
# In-degree List
# ready to take course list: any courses with 0 prerequisites

from collections import deque

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # map each course to it's preprequisite list
    pre_map = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        pre_map[course].append(prereq)

    # step 2 : Track visit state : 0 = unvisited, 1 = viting, 2 = visited
    visited = {}
    
    def dfs(course : int) -> bool:
        # If already in the current path , we found the cycle !
        if visited.get(course, 0) == 1:
            return False
        if visited.get(course, 0) == 2:
            return True
        
        # mark the current course as visiting
        visited[course] = 1

        for prereq in pre_map[course]:
            if not dfs(prereq):
                return False
            
        # mark the current course as visited
        visited[course] = 2
        return True
    
    # check every course to handle disconnected components
    for c in range(numCourses):
        if not dfs(c):
            return False
        
    return True


if __name__ == "__main__":
    num_courses = 2
    prereqs = [[1, 0]]
    
    result = canFinish(num_courses, prereqs)
    print(f"Can finish all courses?: {result}")
    
    assert result == True, "Test Failed"
    print("Success: Course Schedule cycle detection verified.")

    