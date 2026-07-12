# problem - an fresh orange that is 4 - directionally adjacent to a rotten orange becomes rotten. 
# if impossible -1.
# The Strategy - multi source BFS
# why not DFS, because DFS is a maze runner, it dives deep. 
# this problem is about simulataneous spread. the rotting happens level by level.
# all rotten oranges rot their neighbors at the same time. So we need to use BFS.
# Initialize : Add all initially rotten oranges to a queue. count all fresh oranges.
# Spread : Perform BFS. Each "level" of queue represent one minute
# Final check : If there are still fresh oranges left, return -1.

from collections import deque

def rotting_oranges(grid: list[list[int]]) -> int:
    """
    Returns the minimum number of minutes that must elapse until no cell has a fresh oranges.
    Time Complexity: O(m*n) - we visit each cell once.
    Space Complexity: O(m*n) - in the worst case we have to store all cells in the queue
    """

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges = 0

    # initialize the queue with all rotten oranges and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r,c))
            elif grid[r][c] == 1:
                fresh_oranges += 1

    # if there are no fresh oranges, return 0
    if fresh_oranges == 0: return 0

    minutes = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)] # 4 - directiona movement

    # bfs : spread the rotting
    while queue and fresh_oranges > 0:
        minutes += 1
        for _ in range(len(queue)):
            r,c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+ dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append((nr, nc))

    return minutes if fresh_oranges == 0 else -1

if __name__ == "__main__":
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    print(rotting_oranges(grid))  # Output: 4