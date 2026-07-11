# The Problem: given an mxn binary grid, return the maximum area of an island. An island is a group of 1's (land) connected 4-directionally. IF no land exists retturn 0.
# strategy : dfs with return value.

def max_area_of_island(grid: list[list[str]]) -> int:
    """
    Finds the maxiximum area of an island in a binary grid
    TIme complexity: O(m*n) - we visit each cell once.
    Space Complexity: O(mxn) - in the worst case we hace to store all cells in the recursion stack.
    """

    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    max_area = 0
    def dfs(r,c) -> int:
        if r < 0 or r>= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return 0
        
        
        # sink the land we dont count it again
        grid[r][c] = "0"

        return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                max_area = max(max_area, dfs(r,c))


    return max_area

if __name__ == "__main__":
    grid = [
        ["0","0","1","0"],
        ["1","1","1","0"],
        ["0","1","0","0"]
        ]
    print(max_area_of_island(grid))
