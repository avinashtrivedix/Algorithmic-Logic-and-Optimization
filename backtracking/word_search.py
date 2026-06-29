# given an m x n grid if characters called board and a string word, return True if word exists in the grid
# the word can be contructed from letter if sequentially adjacent cells, where "sequential adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once within a single word  mactch path 

def exist(board : list[list[str]], word: str) -> bool:
    
    """
    determines if a target word exists within a 2d character grid using grid_based backtraking.
    Time Complexity : O(m*n*4^L) - where m, n are are board dimentions and L is word length.
    Space Complexity : O(L) - the maximum depth limit of the execution recursion stack from stack.
    """

    rows, cols = len(board) , len(board[0])
    def _dfs(r:int, c:int, k:int) -> bool:
        # Base Case 1 : The entire word matching characters string sequence has been filly processed
        if k == len(word):
            return True
        
        #Base Case 2 : Boundary check failures, mismatching valules, stepping on a visited cell "#"
        if (r < 0 or r >= rows or 
            c < 0 or c >= rows or 
            board[r][c] != word[k]):
            return False

        # 1. choose- save the original state value and temporarily modify the cell block to block self intersection
        temp = board[r][c]
        board[r][c] = "#"

        # 2. Explore - Dive 4 directionally to check if any neighbor branch path can complete the match
        found = (_dfs(r+1, c, k+1) or #down
                 _dfs(r-1, c, k+1) or #up
                 _dfs(r, c+1, k+1) or #right
                 _dfs(r, c-1, k+1))   #left
        
        #3. Unchoose - (Backtrack cleanup) : Restore cell value back to oriignal state for other starting scans
        board[r][c] = temp

        return found
    
    # scan every coordinate index coordinate on teh boord layout matrix to find valid word anchors
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                if _dfs(r, c, 0):
                    return True
                
    return False


if __name__ == "__main__":
    char_board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    target_word = "ABCCED"
    
    word_exists = exist(char_board, target_word)
    print(f"Does the word '{target_word}' exist on the board? {word_exists}")  # Expected: True