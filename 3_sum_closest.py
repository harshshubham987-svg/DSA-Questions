'''
16. 3Sum Closest

Given an integer array nums of length n and an integer target,
find three integers such that the sum is closest to target.

Return that closest sum.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
'''

# Solution:

nums = [-1,2,1,-4]
target = 1

# Length of array
n = len(nums)

# Assume first three elements as initial answer
ans = nums[0] + nums[1] + nums[2]

# Sort array for two-pointer approach
nums.sort()

# Traverse each element
for i in range(n - 2):

    # Start pointer
    s = i + 1

    # End pointer
    e = n - 1

    # Apply two-pointer search
    while s < e:

        # Calculate current sum
        num = nums[i] + nums[s] + nums[e]

        # Current distance from target
        dis = abs(target - num)

        # Best distance so far
        best = abs(target - ans)

        # Update answer if current sum is closer
        if dis < best:
            ans = num

        # If current sum is smaller than target
        # move start pointer right
        if num < target:
            s += 1

        # If current sum is greater than target
        # move end pointer left
        elif num > target:
            e -= 1
        
        # Exact match found
        else:
            print(num)
            exit()

# Print final closest sum
print(ans)

# Time Complexity: O(n²)
# Space Complexity: O(1)

'''
Theory Explanation:

1. This problem is similar to 3Sum.

2. Difference:
   Instead of finding sum = 0,
   we find sum closest to target.

3. First sort the array.

4. Fix one element.

5. Use two pointers:
   s = i+1
   e = last index

6. Calculate current sum.

7. Compare:
   abs(target - current_sum)

   with

   abs(target - best_answer)

8. Update answer if current sum is better.

Pointer movement:

-> If current sum < target:
   Move s forward to increase sum.

-> If current sum > target:
   Move e backward to decrease sum.

-> If equal:
   That is the best possible answer.

Important Steps:

-> Sorting is necessary.
-> Always compare absolute difference.
-> Two pointers reduce brute force O(n³) to O(n²).

Key Intuition:

Fix one number,
then use two pointers to find the closest remaining pair.
'''