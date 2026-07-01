'''
18. 4Sum

Given an array nums of n integers,
return all unique quadruplets [a,b,c,d]
such that:

nums[a] + nums[b] + nums[c] + nums[d] == target

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

# solution

nums = [1,0,-1,0,-2,2]
target = 0

# Length of array
n = len(nums)

# Store final quadruplets
ans = []

# Sort array for two-pointer approach
nums.sort()

# Fix first element
for i in range(n - 3):

    # Skip duplicate values for i
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    # Fix second element
    for j in range(i + 1, n - 2):

        # Start pointer
        s = j + 1

        # End pointer
        e = n - 1

        # Skip duplicate values for j
        if j != i + 1 and nums[j] == nums[j - 1]:
            continue

        # Apply two-pointer search
        while s < e:

            # Calculate total sum
            num = nums[i] + nums[j] + nums[s] + nums[e]

            # If target found
            if num == target:

                # Store valid quadruplet
                ans.append([nums[i], nums[j], nums[s], nums[e]])

                # Move both pointers
                s += 1
                e -= 1

                # Skip duplicate values for s
                while s < e and nums[s] == nums[s - 1]:
                    s += 1

                # Skip duplicate values for e
                while s < e and nums[e] == nums[e + 1]:
                    e -= 1

            # Need bigger sum
            elif num < target:
                s += 1

            # Need smaller sum
            else:
                e -= 1

# Print final answer
print(ans)

# Time Complexity: O(n³)
# Space Complexity: O(1) (excluding output)

'''
Theory Explanation:

1. This problem is extension of 3Sum.

2. Instead of fixing 1 element,
   we fix 2 elements.

3. After fixing:
   Remaining problem becomes Two Sum.

4. Steps:

   -> Sort array
   -> Fix first number (i)
   -> Fix second number (j)
   -> Use two pointers for remaining

5. Cases:

-> total == target
   Store answer.

-> total < target
   Move start pointer.

-> total > target
   Move end pointer.

6. Duplicate skipping is important
   for i, j, s, e.

Important Steps:

-> Sort first.
-> Skip duplicates at every level.
-> Use two pointers for optimization.

Key Intuition:

Fix two numbers,
solve remaining two with two-pointer.
Brute force O(n⁴) becomes O(n³).
'''