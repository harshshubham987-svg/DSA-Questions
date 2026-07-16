'''
542. 01 Matrix

Given an m x n binary matrix mat.

For every cell,
find the distance
to the nearest 0.

Distance is calculated using
4-directional movement:

-> Up
-> Down
-> Left
-> Right

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
'''

# Solution

from collections import deque


def main():

    # Input matrix
    mat = [[0,0,0],
           [0,1,0],
           [1,1,1]]

    # Number of rows
    m = len(mat)

    # Number of columns
    n = len(mat[0])

    # Store final distances
    result = [["_"] * n for _ in range(m)]

    # Current BFS distance
    dis = 0

    # Queue for BFS
    q = deque()

    # Store visited cells
    visit = set()

    # Push all zero cells into queue
    for i in range(m):
        for j in range(n):

            if mat[i][j] == 0:
                q.append((i, j))
                visit.add((i, j))

    # Apply Multi-Source BFS
    while q:

        # Number of nodes in current BFS level
        size = len(q)

        # Process one BFS level
        for _ in range(size):

            # Remove current cell
            row, col = q.popleft()

            # Store current distance
            result[row][col] = dis

            # Check upper cell
            r = row - 1
            if r >= 0 and (r, col) not in visit:
                q.append((r, col))
                visit.add((r, col))

            # Check lower cell
            r = row + 1
            if r < m and (r, col) not in visit:
                q.append((r, col))
                visit.add((r, col))

            # Check left cell
            c = col - 1
            if c >= 0 and (row, c) not in visit:
                q.append((row, c))
                visit.add((row, c))

            # Check right cell
            c = col + 1
            if c < n and (row, c) not in visit:
                q.append((row, c))
                visit.add((row, c))

        # Move to next BFS level
        dis += 1

    # Return final distance matrix
    return result


# Main function execution
if __name__ == "__main__":
    print(main())

# Time Complexity: O(m × n)
# Space Complexity: O(m × n)

'''
Theory Explanation:

1. This problem uses Multi-Source BFS.

2. Instead of starting BFS
   from every cell containing 1,

   start BFS from every cell
   containing 0.

3. All zero cells are added
   into the queue initially.

4. Every BFS level represents
   one unit of distance.

5. First level:

   All zero cells.

   Distance = 0

6. Second level:

   Cells one step away from zero.

   Distance = 1

7. Third level:

   Cells two steps away.

   Distance = 2

8. Continue until
   the queue becomes empty.

9. Since BFS visits cells
   level by level,

   the first time a cell is visited
   is always its shortest distance
   from any zero.

10. visited prevents
    processing the same cell twice.

Important Steps:

-> Push all zeros first.
-> Use Multi-Source BFS.
-> One BFS level = one distance.
-> Mark visited immediately.
-> Store distance when popping from queue.

Key Intuition:

Instead of asking:

"How far is every 1 from a 0?"

Reverse the thinking:

"Let every 0 spread outward together."

The first time a cell is reached
is automatically
its shortest distance to a zero.

Pattern:

Multi-Source BFS
+
Level Order Traversal
+
Grid Expansion
=
Nearest Zero Distance
'''