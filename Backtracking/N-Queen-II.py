'''
52. N-Queens II

The n-queens puzzle is the problem of placing n queens
on an n x n chessboard such that no two queens attack each other.

Return the total number of distinct solutions.

Example 1:

Input: n = 4
Output: 2

Example 2:

Input: n = 1
Output: 1
'''

# Solution:

def queen(arr, n, row):

    # If all queens are placed,
    # one valid solution is found
    if row == n:
        return 1

    # Store total valid solutions
    count = 0

    # Try placing queen in every column
    for col in range(len(arr[0])):

        # Assume current position is safe
        place = True

        # Check upper column
        r = row - 1
        while r >= 0:
            if arr[r][col] == "Q":
                place = False
            r -= 1

        # Check left diagonal
        r = row - 1
        c = col - 1
        while r >= 0 and c >= 0:
            if arr[r][c] == "Q":
                place = False
            r -= 1
            c -= 1

        # Check right diagonal
        r = row - 1
        c = col + 1
        while r >= 0 and c < len(arr[0]):
            if arr[r][c] == "Q":
                place = False

            r -= 1
            c += 1

        # If current position is safe
        if place:

            # Place queen
            arr[row][col] = "Q"

            # Count solutions for remaining rows
            co = queen(arr, n, row + 1)

            # Backtrack by removing queen
            arr[row][col] = "."

            # Add returned solutions
            count += co

    # Return total solutions
    return count


def main():

    # Board size
    n = 4

    # Create empty chess board
    board = [["."] * n for _ in range(n)]

    # Count total solutions
    count = queen(board, n, 0)

    # Print final answer
    print(count)


# Main function execution
if __name__ == "__main__":
    main()

# Time Complexity: O(N!)
# Space Complexity: O(N²)

'''
Theory Explanation:

1. This problem uses Backtracking.

2. Place one queen in each row.

3. Before placing a queen,
   check whether the position is safe.

4. Safe means:
   -> No queen in same column.
   -> No queen in left diagonal.
   -> No queen in right diagonal.

5. If safe:
   -> Place queen.
   -> Solve next row recursively.

6. After recursion:
   Remove queen (Backtracking)
   and try next column.

7. If row becomes equal to n:
   One complete solution is found,
   so return 1.

8. Every recursive call returns
   the number of valid solutions
   from that state.

Important Steps:

-> One queen per row.
-> Check only upper rows.
-> Backtracking restores board.
-> Add returned counts from recursion.

Key Intuition:

Instead of storing every valid board,
count each completed arrangement.
Every successful recursive path contributes
one valid solution.
'''