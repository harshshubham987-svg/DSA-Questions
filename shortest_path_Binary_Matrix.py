'''
1091. Shortest Path in Binary Matrix

Given an n x n binary matrix grid.

0 -> Empty cell
1 -> Blocked cell

Find the length of the shortest path
from the top-left cell
to the bottom-right cell.

Movement is allowed in
8 directions:

-> Up
-> Down
-> Left
-> Right
-> Top-Left
-> Top-Right
-> Bottom-Left
-> Bottom-Right

Return -1 if no path exists.

Example 1:

Input:
[[0,1],
 [1,0]]

Output:
2

Example 2:

Input:
[[0,0,0],
 [1,1,0],
 [1,1,0]]

Output:
4
'''

# Solution

from collections import deque

def main():

    # Input grid
    grid = [[0,0,0],
            [1,1,0],
            [1,1,0]]

    # Store current path length
    path = 0

    # Queue for BFS
    q = deque()

    # Destination row
    nr = len(grid) - 1

    # Destination column
    nc = len(grid[0]) - 1

    # Check starting cell
    if grid[0][0] == 0:
        q.append((0,0))
    else:
        return -1

    # Store visited cells
    visit = set()
    visit.add((0,0))

    # Apply BFS
    while q:

        # One BFS level represents one path length
        path += 1

        # Number of cells in current level
        size = len(q)

        print("Visit : ", visit)

        # Process current BFS level
        for _ in range(size):

            # Remove current cell
            row, col = q.popleft()

            # Destination reached
            if row == nr and col == nc:
                return path

            # Check upper cell
            r = row - 1
            if r >= 0 and grid[r][col] == 0 and (r, col) not in visit:
                q.append((r, col))
                visit.add((r, col))

            # Check lower cell
            r = row + 1
            if r < len(grid) and grid[r][col] == 0 and (r, col) not in visit:
                q.append((r, col))
                visit.add((r, col))

            # Check left cell
            c = col - 1
            if c >= 0 and grid[row][c] == 0 and (row, c) not in visit:
                q.append((row, c))
                visit.add((row, c))

            # Check right cell
            c = col + 1
            if c < len(grid[0]) and grid[row][c] == 0 and (row, c) not in visit:
                q.append((row, c))
                visit.add((row, c))

            # Check upper-left diagonal
            r = row - 1
            c = col - 1
            if r >= 0 and c >= 0 and grid[r][c] == 0 and (r, c) not in visit:
                q.append((r, c))
                visit.add((r, c))

            # Check lower-left diagonal
            r = row + 1
            c = col - 1
            if r < len(grid) and c >= 0 and grid[r][c] == 0 and (r, c) not in visit:
                q.append((r, c))
                visit.add((r, c))

            # Check upper-right diagonal
            r = row - 1
            c = col + 1
            if r >= 0 and c < len(grid[0]) and grid[r][c] == 0 and (r, c) not in visit:
                q.append((r, c))
                visit.add((r, c))

            # Check lower-right diagonal
            r = row + 1
            c = col + 1
            if r < len(grid) and c < len(grid[0]) and grid[r][c] == 0 and (r, c) not in visit:
                q.append((r, c))
                visit.add((r, c))

        print("Queue : ", q)

    # Destination not reachable
    return -1


# Main function execution
if __name__ == "__main__":
    print(main())

# Time Complexity: O(n²)
# Space Complexity: O(n²)

'''
Theory Explanation:

1. This problem uses BFS (Breadth First Search).

2. BFS is used because
   we need the shortest path.

3. Start BFS
   from (0,0).

4. If starting cell is blocked (1),
   return -1 immediately.

5. Queue stores cells
   to be explored.

6. Visited set prevents
   revisiting the same cell.

7. One complete BFS level
   represents one path length.

8. For every cell,
   check all 8 directions:

   -> Up
   -> Down
   -> Left
   -> Right
   -> Upper Left
   -> Upper Right
   -> Lower Left
   -> Lower Right

9. If neighbour:

   -> Inside boundary
   -> Is 0
   -> Not visited

   Add it into queue.

10. When destination is reached,
    current path length
    is the shortest path.

11. If queue becomes empty,
    no path exists.

Important Steps:

-> BFS guarantees shortest path.
-> Mark visited immediately after pushing.
-> Process one BFS level at a time.
-> Check all 8 directions.
-> Return -1 if destination is unreachable.

Key Intuition:

Think of the grid
as an unweighted graph.

Each move costs 1.

BFS always reaches the destination
using the minimum number of steps.

Pattern:

Grid
+
8-Direction BFS
+
Level Order Traversal
=
Shortest Path
'''