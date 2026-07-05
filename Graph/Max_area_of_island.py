'''
695. Max Area of Island

You are given an m x n binary matrix grid.

An island is formed by connecting
adjacent lands (1's) horizontally
or vertically.

The area of an island is the total
number of connected land cells.

Return the maximum area of any island.

Example 1:

Input:
grid = [
[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]
]

Output: 6

Example 2:

Input:
grid = [[0,0,0,0,0,0,0,0]]

Output: 0
'''

# Solution

def dfs(arr, row, col):

    # Return if indices go outside the grid
    if row < 0 or row >= len(arr) or col < 0 or col >= len(arr[0]):
        return 0

    # Return if current cell is water
    elif arr[row][col] == 0:
        return 0

    # Mark current land as visited
    arr[row][col] = 0

    # Count current land cell
    curr = 1

    # Visit upper cell
    up = dfs(arr, row - 1, col)

    # Visit lower cell
    dow = dfs(arr, row + 1, col)

    # Visit left cell
    lef = dfs(arr, row, col - 1)

    # Visit right cell
    rig = dfs(arr, row, col + 1)

    # Return total area of current island
    return curr + up + dow + lef + rig


def main():

    # Input grid
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]

    # Store maximum island area
    max_count = 0

    # Traverse every cell
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            # Start DFS from every unvisited land
            if grid[i][j] == 1:

                # Find current island area
                a = dfs(grid, i, j)

                print(a)

                # Update maximum area
                max_count = max(max_count, a)

    # Print final answer
    print(max_count)


# Main function execution
if __name__ == "__main__":
    main()

# Time Complexity: O(m × n)
# Space Complexity: O(m × n)   # Recursive call stack (worst case)

'''
Theory Explanation:

1. This problem uses DFS (Depth First Search).

2. Traverse every cell in the grid.

3. Whenever a land (1) is found:
   -> Start DFS.
   -> Count all connected land cells.

4. During DFS:
   -> Mark visited land as 0.
   -> Explore all four directions.

5. Every recursive call returns
   the area contributed by that path.

6. Total island area is:

   current cell
   + up
   + down
   + left
   + right

7. Compare current island area
   with maximum area found so far.

Important Steps:

-> Traverse complete grid.
-> Start DFS only from land.
-> Mark visited land immediately.
-> DFS returns island area.
-> Keep updating maximum area.

Key Intuition:

Instead of only sinking an island,
DFS also counts every connected land cell,
giving the area of that island.
The largest returned area is the answer.
'''