'''
643. Maximum Average Subarray I

You are given an integer array nums and an integer k.

Find the contiguous subarray of length k
that has the maximum average.

Return the maximum average.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000

Example 2:

Input: nums = [5], k = 1
Output: 5.00000
'''

# Solution

nums = [1,12,-5,-6,50,3]
k = 4

# Calculate sum of first window
f_sum = sum(nums[0:k])

# Calculate average of first window
avg = f_sum / float(k)

# Store maximum average
max_avg = avg

# Slide the window through the array
for i in range(k, len(nums)):

    # Update window sum
    f_sum = f_sum + nums[i] - nums[i - k]

    # Calculate current average
    cur_avg = f_sum / float(k)

    # Update maximum average
    max_avg = max(max_avg, cur_avg)

# Print final answer
print(max_avg)

# Time Complexity: O(n)
# Space Complexity: O(1)

'''
Theory Explanation:

1. This problem uses Sliding Window.

2. First calculate:
   Sum of first window of size k.

3. Find its average.

4. Move window one step at a time.

5. While moving:
   -> Add new element.
   -> Remove outgoing element.

6. Calculate new average.

7. Update maximum average.

Important Steps:

-> First window is calculated separately.
-> No need to calculate sum again.
-> Window sum is updated in O(1).
-> Keep tracking maximum average.

Key Intuition:

Instead of recalculating every subarray,
slide one fixed-size window
and update its sum efficiently.
'''