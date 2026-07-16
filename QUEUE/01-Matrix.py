'''542. 01 Matrix
Medium
Topics
premium lock icon
Companies
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
'''

#solution:
from collections import deque

def main():
    mat = [[0,0,0],[0,1,0],[1,1,1]]

    m = len(mat)
    n = len(mat[0])

    result = [["_"]*n for _ in range(m)]

    dis = 0

    q = deque()
    visit = set()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                q.append((i, j))
                visit.add((i, j))

    

    while q:

        size = len(q)
        
        for _ in range(size):
            
            row , col = q.popleft()

            result[row][col] = dis

            #up
            r = row -1
            if r >= 0 and (r, col) not in visit:
                q.append((r, col))
                visit.add((r, col))
            
            # Down:
            r = row + 1
            if r < m and (r, col) not in visit:
                q.append((r, col))
                visit.add((r, col))
            
            # Left
            c = col - 1
            if c >= 0 and (row, c) not in visit:
                q.append((row, c))
                visit.add((row, c))
            
            # Right
            c = col + 1
            if c < n and (row, c) not in visit:
                q.append((row, c))
                visit.add((row, c))


        dis += 1

    return result

if __name__ == "__main__":
    print(main())
