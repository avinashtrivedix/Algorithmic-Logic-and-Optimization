# given a 2d grid of 0 and 1s, how manny islands are there

def num_islands(grid: list[list[str]]) -> int:
    """
    counts the number of islands usinf dfs
    Time Complexity: O(mxn) - each cell is visited once
    Space complexity: O(mxn) - in the worst case, recursion stack can go as deep as the number of cells in the grid.
    """

    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])

    island = 0

    def dfs(r: int, c: int) -> None:
        # base case: check bounds and if current cell is water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        
        #mark as visited: "sink" the land
        grid[r][c] = '0'
        #explore the four directions (up, dowm , right, left)
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    #main loop: iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                island += 1
                dfs(r,c)

    return island

if __name__ == "__main__":
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f"Number of islands : {num_islands(grid)}") #expected 3