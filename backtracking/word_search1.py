# Iterate through ever letter in a grid to find the starting letter of the word.
def exist(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def backtrack(r: int, c : int, i : int) -> bool:
        # base case : we successfully matched every character in the word
        if i == len(word):
            return True
        
        # Boundary check, character mismatch check, or already visited check
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False
        
        # Temporarily mark the cell as visited.
        temp = board[r][c]
        board[r][c] = '#'

        # Explore all four directions : up, dow, left, right
        found = (backtrack(r+1, c, i+1) or
                 backtrack(r-1, c, i+1) or 
                 backtrack(r, c+1, i+1) or
                 backtrack(r, c-1, i+1)
                 )
        
        # backtrack : restore the original character in the cell.
        board[r][c] = temp
        return found
    for r in range(rows):
        for c in range(cols):
            if backtrack(r,c,0):
                return True
            
    return False

if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word = "ABCCED"
    
    result = exist(board, word)
    print(f"Word '{word}' exists in board: {result}")
    
    assert result == True, "Test Failed"
    print("Success: Word Search backtracking verified.")