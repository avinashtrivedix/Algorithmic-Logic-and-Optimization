#Number of island. 
# the story: Given an mxn 2d binary grid which represents a map of '1's (land) and '0' (water)
# return the number of islands. An island is susurrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

def numsIsland(grid: list[list[str]]) -> int:
    if not grid: 
        return 0
    
    rows, col = len(grid), len(grid[0])
    island_count = 0

    def dfs(r: int, c: int):
        # Check for out of bounds or if the cell is water ('0')
        if r < 0 or c < 0 or r >= rows or c >= col or grid[r][c] == '0':
            return
        
        grid[r][c] = '0'

        # Recursively visit all four cardinal directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(col):
            if grid[r][c] == '1':
                island_count += 1
                dfs(r, c)       # Flood-fill the entire connected island


    return island_count



if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    
    result = numsIsland(grid)
    print(f"Number of islands found: {result}")
    
    assert result == 3, "Test Failed"
    print("Success: Number of Islands verified.")