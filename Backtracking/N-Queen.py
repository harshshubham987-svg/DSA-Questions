'''
51. N-Queens

The n-queens puzzle is the problem of placing n queens
on an n x n chessboard such that no two queens attack each other.

Rules:
-> Same column not allowed
-> Same left diagonal not allowed
-> Same right diagonal not allowed

Return all distinct solutions.
'''

# Solution:

def queen(board, n, row, ans):

    # If all rows are filled, store current board
    if row == n:
        ans.append(["".join(r) for r in board])
        return
    
    # Try placing queen in every column of current row
    for col in range(len(board[0])):
        
        # Assume queen can be placed
        place = True

        # Check upward column
        r = row - 1
        while r >= 0:
            if board[r][col] == "Q":
                place = False
            r -= 1
        
        # Check left diagonal
        r = row - 1
        c = col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                place = False
            r -= 1
            c -= 1
        
        # Check right diagonal
        r = row - 1
        c = col + 1
        while r >= 0 and c < len(board[0]):
            if board[r][c] == "Q":
                place = False
            
            r -= 1
            c += 1
        
        # If safe to place queen
        if place:

            # Place queen
            board[row][col] = "Q"

            # Move to next row
            queen(board, n, row + 1, ans)

            # Backtrack and remove queen
            board[row][col] = "."


def main():

    # Board size
    n = 4

    # Store all valid boards
    ans = []

    # Create empty board
    board = [["."] * n for _ in range(n)]

    # Start recursion from row 0
    queen(board, n, 0, ans)

    # Print final result
    print(ans)


# Main function execution
main()

# Time Complexity: O(N!)
# Space Complexity: O(N²)

'''
Theory Explanation:

1. This problem uses Backtracking.

2. We place one queen in each row.

3. For each cell:
   Check if placing queen is safe.

4. Safe means:
   -> No queen in same column
   -> No queen in left diagonal
   -> No queen in right diagonal

5. If safe:
   Place queen and move to next row.

6. If next row fails:
   Remove queen (backtrack)
   and try next column.

7. If all rows are filled:
   Store the board.

Important Steps:

-> One queen per row.
-> Only check upper rows because lower rows are empty.
-> Backtracking restores board state.
-> Convert rows into string before storing.

Key Intuition:

Try every possible placement row by row.
If invalid, undo and try another.
This explores all possible valid boards.
'''