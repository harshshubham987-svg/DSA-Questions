'''
55. Jump Game

You are given an integer array nums.

Each element represents the maximum jump length
from that position.

Return True if you can reach
the last index,
otherwise return False.

Example 1:

Input: nums = [2,3,1,1,4]
Output: True

Example 2:

Input: nums = [3,2,1,0,4]
Output: False
'''

# Solution

def main():

    # Input array
    nums = [3,2,1,0,4]

    # Assume last index is reachable
    jump = True

    # Store the farthest reachable index
    max_reach = 0

    # Traverse every index
    for i in range(len(nums)):

        # If current index cannot be reached,
        # jumping is impossible
        if not i <= max_reach:
            jump = False
            break

        # Calculate farthest position
        # reachable from current index
        curr = i + nums[i]

        # Update maximum reachable index
        max_reach = max(max_reach, curr)

    # Return final answer
    return jump


# Print final result
print(main())

# Time Complexity: O(n)
# Space Complexity: O(1)

'''
Theory Explanation:

1. This problem uses Greedy.

2. Keep track of the farthest index
   that can be reached.

3. Traverse the array from left to right.

4. At every index:

   -> If current index is greater than
      max_reach,
      then this index is unreachable.

   -> Otherwise,
      update max_reach using:

      current index + jump length

5. Continue until the end.

Important Steps:

-> max_reach stores the farthest reachable position.
-> Every reachable index helps extend the range.
-> If an index cannot be reached,
   answer becomes False.
-> No need to simulate every jump.

Key Intuition:

Instead of deciding
which jump to take,
keep extending the farthest position
you can possibly reach.
If every index is reachable,
the last index is also reachable.
'''