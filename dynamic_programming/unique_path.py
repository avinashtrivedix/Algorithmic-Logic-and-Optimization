# the prroblem - there is a robot o an m x n grid. The robot is initially located at the top-left corner (0,0). 
# the robot tries the bottom right corner (m-1, n-1). the robot can only move down or right at any point in time.
# given the two integer m and n (which is the total dimension of the board) , 
# return the number of possible unique paths that the robot can take to reach the bottom right corner
# we reach the answer not by counting every single path one by one (that would take forever), 
# but by labelling each square with the number of ways to reach it.
# imagine you are standing on a grid. to get to any square, 
# you must have come from square directly above you or the square directly to your left.
# instead of thinking where the robot can go , think about how it could have arrived at a specific cell. to arrive at cell(r,c), 
# the robot could have come form the grid above it (r-1, c) or (c, r-1)
# the formula = dp[r][c] = dp[r-1][c] + dp[r][c-1]
# base case : Every cell in teh first row and the forst column  has exactly 1 way to be reached (by just moving striangh right ir straight down)
# space optimization  :  we dont need full mxn matrix. we only need the current row and the previous row value to calculate the next step. 
# allowing us to reduce space complexity to O(n).


def unique_paths(m: int, n: int) -> int:
    """
    Calculate the the nuber iof unique paths from top-left to bottom-right in a grid.
    Time Complexity: O(m*n)
    Space Complexity: o(n)
    """
    # create a single row initizaed to 1s
    dp = [1]*n

    #we already initialized the first row, so we iterate remaining m-1 rows
    for i in range (1,m):
        for j in range (1,n):
            # the value of dp[j] (current cell) is its current value from above
            # plus teh value of[j-1] (the cell to the left)
            dp[j] = dp[j] + dp[j-1]

    return dp[n-1]

if __name__ == "__main__":
    m, n = 3,7
    print(f"Unique paths for {m}x{n} grid: {unique_paths(m, n)}") # Expected: 28