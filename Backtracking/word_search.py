'''79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false'''

# Solution:

def dfs(board, word, indx, row, col, visited):

    # If current cell is already visited
    if (row, col) in visited:
        return False

    # If all characters are matched
    if indx == len(word):
        return True

    # Mark current cell as visited
    visited.add((row, col))

    # Check left
    if col > 0:
        if board[row][col - 1] == word[indx]:

            if dfs(board, word, indx + 1, row, col - 1, visited):
                visited.remove((row, col))
                return True

    # Check right
    if col < (len(board[0]) - 1):
        if board[row][col + 1] == word[indx]:

            if dfs(board, word, indx + 1, row, col + 1, visited):
                visited.remove((row, col))
                return True

    # Check up
    if row > 0:
        if board[row - 1][col] == word[indx]:

            if dfs(board, word, indx + 1, row - 1, col, visited):
                visited.remove((row, col))
                return True

    # Check down
    if row < (len(board) - 1):
        if board[row + 1][col] == word[indx]:

            if dfs(board, word, indx + 1, row + 1, col, visited):
                visited.remove((row, col))
                return True

    # Backtrack if no path found
    visited.remove((row, col))

    return False


def main():

    # Input board
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]

    # Target word
    word = "ABCB"

    # Traverse whole board
    for i in range(len(board)):
        for j in range(len(board[0])):

            # Start DFS if first character matches
            if board[i][j] == word[0]:

                if dfs(board, word, 1, i, j, set()):
                    return True

    return False


# Print final result
print(main())

# Time Complexity: O(m * n * 4^L)
# Space Complexity: O(L)

'''
Theory Explanation:

1. This problem uses DFS + Backtracking.

2. Idea:
   Start from every cell that matches first character.

3. From each starting point:
   Explore 4 directions:
   -> Left
   -> Right
   -> Up
   -> Down

4. If next character matches:
   Continue DFS.

5. Use visited set:
   So same cell is not reused.

6. If path fails:
   Backtrack by removing cell from visited.

Important Steps:

-> Start DFS only when first character matches.
-> Check boundaries before moving.
-> Mark visited before recursion.
-> Remove visited after recursion.

Key Intuition:

Try every possible path,
and backtrack when path becomes invalid.
This explores all valid combinations.
'''