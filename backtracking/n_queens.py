# the problem of placing n - queens in a chess board, so that no queen attack each other.
"""
the chess rule-
the queen can attack horiziontally, vertically and diagonally.
no two queens can share the same row or columns 
no 2 queen can share the positive or negatice diagonal
"""
def solve_n_queens(n:int) -> list[list[str]]:
    """
    solves the N-queens placement problem using row-by-row backtracking and mathematical diagonal sets.
    Time Complexity: O(n!) - The search space shrinks by atleast one columsn choice at each row tier.
    Space Complesity: O(N^2) - Required for the board configurationmatrix and sets
    """

    res = []

    #Global state tracking sets to protect lines of sight
    cols = set()
    pos_diag = set() # r+c constant
    neg_diag = set() # ric constant

    # Initialize an empty board filled with dots
    board = [["."] * n for _ in range(n)]

    def _backtrack(r : int) -> None:
        #Base case : All nrows have been successfully populated with the safe queens
        if r == n:
            # convert rows arrays back to standard strings. converts 2D grid of characters into a clean list of text strings. then saves that layout to your list of successful soulution.
            res.append(["".join(row) for row in board])
            return
        
        # Scan across every column index option for the current row
        for c in range(n):
            # if the column and diagonals are under attack skip this placement choice.
            if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                continue

            # 1. Choose: Lock down the column and Diagonal and update the board grid
            cols.add(c)
            pos_diag.add(r+c)
            neg_diag.add(r-c)
            board[r][c]="Q"

            #2. Explore: Mpve down to the next row tier.
            _backtrack(r+1)

            #3. Unchoose: (Backtrack clean up) - strip the queen and release the consttraints
            cols.remove(c)
            pos_diag.remove(r+c)
            neg_diag.remove(r-c)
            board[r][c] = "."

    _backtrack(0)
    return res

if __name__ == "__main__":
    board_size = 4
    solutions = solve_n_queens(board_size)

    print(f"Total Unique solutions found do {board_size}x{board_size}board : {len(solutions)}")
    for idx, sol in enumerate(solutions):
        print(f"\nSolution Configuration {idx +1}:")
        for row in sol:
            print(row)