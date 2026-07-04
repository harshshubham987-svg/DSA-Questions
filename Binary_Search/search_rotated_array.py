'''
33. Search in Rotated Sorted Array

Given a rotated sorted array nums and a target,
return its index if found,
otherwise return -1.

Time Complexity must be O(log n).

Example:
nums = [4,5,6,7,0,1,2]
target = 0
Output = 4
'''

# Solution:

nums = [6,7,0,1,2,4,5]
target = 0

# Left pointer
lef = 0

# Right pointer
rig = len(nums) - 1

# Store answer
ans = -1

# Apply binary search
while lef <= rig:

    # Find middle index
    mid = (rig + lef) // 2

    # Target found
    if nums[mid] == target:
        ans = mid
        break

    # Check if left half is sorted
    elif nums[mid] >= nums[lef]:

        # Target lies inside left sorted half
        if target >= nums[lef] and target < nums[mid]:
            rig = mid - 1

        # Search in right half
        else:
            lef = mid + 1

    # Otherwise right half is sorted
    else:

        # Target lies inside right sorted half
        if target > nums[mid] and target <= nums[rig]:
            lef = mid + 1

        # Search in left half
        else:
            rig = mid - 1

# Print final answer
print(ans)

# Time Complexity: O(log n)
# Space Complexity: O(1)

'''
Theory Explanation:

1. This problem uses Modified Binary Search.

2. Even after rotation,
   one half of the array is always sorted.

3. At every iteration:

   -> Find middle element.

   -> Check which half is sorted.

4. If left half is sorted:

   Check whether target lies between:
   nums[left] and nums[mid].

   If yes:
      Search left half.

   Otherwise:
      Search right half.

5. If right half is sorted:

   Check whether target lies between:
   nums[mid] and nums[right].

   If yes:
      Search right half.

   Otherwise:
      Search left half.

Important Steps:

-> One half is always sorted.
-> Identify the sorted half first.
-> Check if target belongs to that half.
-> Eliminate half of the search space each iteration.

Key Intuition:

Treat the rotated array
as two sorted halves.
Every step, identify the sorted half
and continue binary search there.
'''