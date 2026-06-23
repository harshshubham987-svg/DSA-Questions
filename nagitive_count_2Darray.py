'''1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.


Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 '''

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

# Store total negative numbers
count = 0

# Traverse each row of the grid
for i in range(len(grid)):
    
    # Start from the last column of current row
    j = len(grid[0]) - 1

    # Move backward until column index is valid
    while j >= 0:
        
        # Get current number
        num = grid[i][j]

        # Check if current number is negative
        if num < 0:
            count += 1
        else:
            # Stop checking current row if positive number found
            break
    
        # Move to previous column
        j -= 1

# Print total count of negative numbers
print(count)

# Time Complexity: O(m × n)
# Space Complexity: O(1)