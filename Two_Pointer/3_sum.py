'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that:
i != j, i != k, and j != k
and nums[i] + nums[j] + nums[k] == 0.

The solution must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = [0,1,1]
Output: []

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
'''

# Solution:

nums = [-1,0,1,2,-1,-4]

# Length of array
n = len(nums)

# Store final triplets
ans = []

# Sort array for two-pointer approach
nums.sort()

# Traverse each element
for i in range(n - 2):

    # Start pointer after current element
    s = i + 1

    # End pointer at last index
    e = n - 1

    # Skip duplicate values for i
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    # Apply two-pointer search
    while s < e:

        # Calculate total sum
        num = nums[i] + nums[s] + nums[e]

        # If sum becomes 0
        if num == 0:

            # Store valid triplet
            ans.append([nums[i], nums[s], nums[e]])

            # Move both pointers
            s += 1
            e -= 1

            # Skip duplicate values for start pointer
            while s < e and nums[s] == nums[s - 1]:
                s += 1

            # Skip duplicate values for end pointer
            while s < e and nums[e] == nums[e + 1]:
                e -= 1

        # If sum is smaller than 0
        elif num < 0:
            s += 1

        # If sum is greater than 0
        else:
            e -= 1

# Print final answer
print(ans)

# Time Complexity: O(n²)
# Space Complexity: O(1) (excluding output)

'''
Theory Explanation:

1. This problem uses Sorting + Two Pointer.

2. First sort the array.
   This helps in:
   -> Using two pointers
   -> Skipping duplicates

3. Fix one element nums[i].

4. Use two pointers:
   s = i+1
   e = last index

5. Calculate:
   total = nums[i] + nums[s] + nums[e]

Cases:

-> total == 0
   Found a triplet.

-> total < 0
   Need bigger value.
   Move s forward.

-> total > 0
   Need smaller value.
   Move e backward.

6. Skip duplicates:
   Important to avoid repeated triplets.

Important Steps:

-> Sort before applying two pointers.
-> Fix one element at a time.
-> Skip duplicate i values.
-> Skip duplicate s and e values after finding answer.

Key Intuition:

Fix one number,
then reduce the remaining problem into Two Sum.
That makes brute force O(n³) become O(n²).
'''