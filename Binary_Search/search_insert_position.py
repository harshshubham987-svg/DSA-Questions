'''35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4'''

# solution :- 

nums = [1, 3, 5, 6]
target = 2

# Start pointer
s = 0

# End pointer
e = len(nums)-1

# Store the answer (index of target or insert position)
ans = 0

# Binary search until start crosses end
while s <= e:
    
    # Find middle index
    mid = (s+e)//2

    # If target is found, store index and stop
    if nums[mid] == target:
        ans = mid
        break
    
    # If target is greater, move to right half
    elif nums[mid] < target:
        ans = mid + 1
        s = mid + 1
    
    # If target is smaller, move to left half
    else:
        e = mid - 1

# Print the final position
print(ans)

# Time Complexity: O(log n)
# Space Complexity: O(1)