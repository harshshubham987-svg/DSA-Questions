'''
494. Target Sum

You are given an integer array nums
and an integer target.

Place either '+' or '-'
before every number.

Return the total number of expressions
whose result equals target.

Example 1:

Input:
nums = [1,1,1,1,1]
target = 3

Output:
5

Example 2:

Input:
nums = [1]
target = 1

Output:
1
'''

# Solution

def dfs(nums, i, tar, cur):

    # If all numbers are processed
    if i == len(nums):

        # Valid expression found
        if cur == tar:
            return 1

        # Invalid expression
        return 0

    # Choose '+' for current number
    pos = dfs(nums, i + 1, tar, cur + nums[i])

    # Choose '-' for current number
    neg = dfs(nums, i + 1, tar, cur - nums[i])

    # Return total valid ways
    return pos + neg


def main():

    # Input array
    nums = [1]

    # Target value
    target = 1

    # Count total expressions
    count = dfs(nums, 0, target, 0)

    # Print final answer
    print(count)


# Main function execution
main()

# Time Complexity: O(2^n)
# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses Recursion.

2. For every number,
   we have two choices:

   -> Add (+)
   -> Subtract (-)

3. At each recursive call:

   Current Sum =
   Previous Sum ± Current Number

4. Continue until
   all numbers are used.

5. Base Case:

   If all numbers are processed:

   -> If current sum equals target,
      return 1.

   -> Otherwise,
      return 0.

6. Total ways:

   Ways from '+' choice
   +
   Ways from '-' choice

Important Steps:

-> Every element creates two recursive branches.
-> Current sum keeps changing.
-> Base case checks final answer.
-> Sum both recursive results.

Key Intuition:

For every number,
try both '+' and '-'.

Explore every possible expression,
and count only those
whose final sum equals the target.
'''