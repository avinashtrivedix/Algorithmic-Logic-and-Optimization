# the problem
# given an mxn 2d binary grid which represents a map of '1's (land) and '0's water, 
# return the number if islands. 
# an island is surronded by water and is formed by connecting adjacent lans horizontally and vertically
# the strategy -  depth first search (dfs)
# when you see a grid and need to explore a territory, you use a graph Traversal. 
# An island is just a connected component in a graph.
# 1. iterate : scan evry cell in the grid
# 2. Trigger : when you see a '1', increment your insland_count.
# 3. sink : perform a dfs to sink that island turn all connectet 1 s into 0 so yopu dont count the same land twice.


def num_islands(grid : list[list[str]]) -> int:
    """
    counts the number of islands using dfs
    Time Complexity: O(m*n) - each cell is visited once
    Space Complexity: O(m*n) -  in the worst case (recusrion stack)
    """

    if not grid:
        return 0
    
    rows, cols = len(grid) , len(grid[0])
    islands = 0

    def dfs(r: int, c:int) -> None:
        # base case :  check bounds and if and if cuurrent cell is water
        if r < 0 or r>= rows or c<0 or c>=cols or grid[r][c] =='0':
            return
        
        # mark as visited by sinking the land
        grid[r][c] = '0'

        # explore the neighbors (up, down, left, right)
        dfs(r+1, c) # down 
        dfs(r-1, c) # up
        dfs(r, c+1) # right
        dfs(r, c-1) # left

    for r in range(rows): 
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r,c)

    return islands
    

if __name__ == "__main__":
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f"Number of islands: {num_islands(grid)}") # Expected: 3