'''
200. Number of Islands

Given an m x n binary grid consisting of:
'1' -> Land
'0' -> Water

Return the total number of islands.

An island is formed by connecting
horizontal and vertical lands.

Example 1:
Input:
[
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]
Output: 1

Example 2:
Input:
[
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]
Output: 3
'''

# Solution:

def dfs(arr, row, col):

    # Return if indices go out of grid
    if (row >= len(arr) or row < 0) or (col >= len(arr[0]) or col < 0):
        return

    # Return if current cell is water
    if arr[row][col] == "0":
        return

    # Mark current land as visited
    arr[row][col] = "0"

    # Visit upper cell
    dfs(arr, row - 1, col)

    # Visit lower cell
    dfs(arr, row + 1, col)

    # Visit left cell
    dfs(arr, row, col - 1)

    # Visit right cell
    dfs(arr, row, col + 1)


def main():

    # Input grid
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    # Store total islands
    count = 0

    # Traverse every cell
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            # New island found
            if grid[i][j] == "1":

                # Increase island count
                count += 1

                # Mark complete island as visited
                dfs(grid, i, j)

    # Print total islands
    print(count)


# Main function execution
main()

# Time Complexity: O(m × n)
# Space Complexity: O(m × n)   # Recursive call stack (worst case)

'''
Theory Explanation:

1. This problem uses DFS (Depth First Search).

2. Traverse every cell of the grid.

3. Whenever a land ('1') is found:
   -> It represents a new island.
   -> Increase island count.

4. Start DFS from that land.

5. DFS visits all connected lands
   in four directions:
   -> Up
   -> Down
   -> Left
   -> Right

6. Mark every visited land as '0'
   so it is not counted again.

Important Steps:

-> Traverse complete grid.
-> Start DFS only from land ('1').
-> Mark visited land as water ('0').
-> DFS explores the entire connected island.

Key Intuition:

Whenever you discover an unvisited land,
count it as one island,
then sink the entire island using DFS.
'''