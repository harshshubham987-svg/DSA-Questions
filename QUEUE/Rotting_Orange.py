'''994. Rotting Oranges

You are given an m x n grid where:

0 -> Empty cell
1 -> Fresh orange
2 -> Rotten orange

Every minute,
a fresh orange connected 4-directionally
to a rotten orange becomes rotten.

Return the minimum number of minutes
until no fresh orange remains.

If some fresh orange can never become rotten,
return -1.

Example 1:

Input:
grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]

Output:
4

Example 2:

Input:
grid = [[2,1,1],
        [0,1,1],
        [1,0,1]]

Output:
-1

Example 3:

Input:
grid = [[0,2]]

Output:
0
'''

from collections import deque


def main():

    # Input grid
    grid = [[2,1,1],
            [1,1,0],
            [0,1,1]]

    # Queue stores rotten orange positions
    q = deque()

    # Store total time
    time = 0

    # Traverse complete grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            # Add all initially rotten oranges into queue
            if grid[i][j] == 2:
                q.append((i, j))


    # Process rotten oranges level by level
    while q:

        # Store number of rotten oranges
        # present at current minute
        size = len(q)

        # Track whether any fresh orange
        # becomes rotten in current minute
        rotten = False

        # Process only current BFS level
        for _ in range(size):

            # Remove rotten orange from queue
            row, col = q.popleft()

            # Check upper cell
            r = row - 1

            # If upper orange is fresh
            if r >= 0 and grid[r][col] == 1:

                # Make orange rotten
                grid[r][col] = 2

                # Add newly rotten orange into queue
                q.append((r, col))

                # Mark that rotting happened
                rotten = True


            # Check lower cell
            r = row + 1

            # If lower orange is fresh
            if r < len(grid) and grid[r][col] == 1:

                # Make orange rotten
                grid[r][col] = 2

                # Add newly rotten orange into queue
                q.append((r, col))

                # Mark that rotting happened
                rotten = True


            # Check left cell
            c = col - 1

            # If left orange is fresh
            if c >= 0 and grid[row][c] == 1:

                # Make orange rotten
                grid[row][c] = 2

                # Add newly rotten orange into queue
                q.append((row, c))

                # Mark that rotting happened
                rotten = True


            # Check right cell
            c = col + 1

            # If right orange is fresh
            if c < len(grid[0]) and grid[row][c] == 1:

                # Make orange rotten
                grid[row][c] = 2

                # Add newly rotten orange into queue
                q.append((row, c))

                # Mark that rotting happened
                rotten = True


        # Increase time only if
        # at least one orange became rotten
        if rotten:
            time += 1


    # Check complete grid again
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            # If any fresh orange still exists
            if grid[i][j] == 1:
                return -1


    # Return minimum time
    return time


# Main function execution
if __name__ == "__main__":
    print(main())


# Time Complexity: O(m × n)
# Space Complexity: O(m × n)


'''
Theory Explanation:

1. This problem uses Multi-Source BFS.

2. Why Multi-Source BFS?

   There can be multiple rotten oranges
   at the beginning.

Example:

2 1 1
1 1 2

Both rotten oranges start spreading
at the same time.

Therefore,
all initial rotten oranges
must be added into the queue first.

3. Queue stores:

   (row, column)

   of rotten oranges.

4. BFS is processed level by level.

   One BFS level represents one minute.

5. Before processing a level:

   size = len(q)

   This stores the number of rotten oranges
   that can spread during the current minute.

6. Process exactly "size" oranges.

   Newly rotten oranges are added
   into the queue.

   But they are processed
   in the next BFS level.

7. For every rotten orange,
   check four directions:

   -> Up
   -> Down
   -> Left
   -> Right

8. If a fresh orange is found:

   grid[row][col] = 2

   Mark it rotten immediately.

   Then add its position
   into the queue.

9. rotten variable tracks
   whether any fresh orange became rotten
   during the current BFS level.

10. Time increases only when:

    rotten == True

    This prevents adding extra time
    when no new orange becomes rotten.

Example:

grid = [[0,2]]

Queue:

[(0,1)]

Process rotten orange.

No fresh neighbour exists.

rotten = False

Therefore:

time remains 0.

11. After BFS finishes,
    traverse the grid again.

12. If any fresh orange (1) remains:

    return -1

    Because that orange
    cannot be reached by any rotten orange.

Important Steps:

-> Add ALL rotten oranges initially.
-> Use BFS level-by-level.
-> size = len(q) represents current minute.
-> Newly rotten oranges go into next level.
-> Mark orange rotten before adding to queue.
-> Increase time only when rotting happens.
-> Check remaining fresh oranges at the end.

Key Intuition:

All rotten oranges spread
at the same time.

Therefore,
we start BFS from multiple sources.

Each BFS level represents
one minute of infection spread.

Pattern:

Multi-Source BFS
+
Level Order Traversal
+
Grid Traversal
=
Rotting Oranges
'''