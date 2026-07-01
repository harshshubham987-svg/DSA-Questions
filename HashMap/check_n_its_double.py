'''1346. Check If N and Its Double Exist

Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
'''

# solution

arr = [10, 2, 5, 3]

# Store visited numbers
seen = set()

# Default answer
ans = False

# Traverse through the array
for i in arr:
    
    # Check if double of current number exists
    # Or if current number is even and its half exists
    if i * 2 in seen or (i % 2 == 0 and i // 2 in seen):
        ans = True
        break
    
    # Add current number into seen set
    seen.add(i)

# Print final result
print(ans)

# Time Complexity: O(n)
# Space Complexity: O(n)