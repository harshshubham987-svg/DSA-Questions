'''441. Arranging Coins

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.'''

# solution :

n = 5

# Start from the first row
row = 1

# Keep building rows until enough coins are available
while n >= row:
    # Use current row number of coins
    n -= row
    
    # Move to the next row
    row += 1

# Print total complete rows formed
print(row-1)

# Time Complexity: O(√n)
# Space Complexity: O(1)