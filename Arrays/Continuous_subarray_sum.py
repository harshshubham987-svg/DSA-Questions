'''523. Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true

Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true

Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
'''

# Solution


"""=======================Brute Force Approach ==========================="""


def main():

    # Input array
    nums = [23,2,6,4,7]

    # Divisor value
    k = 6

    # Select starting index of subarray
    for i in range(len(nums)):

        # Store current subarray sum
        curr = 0

        # Expand subarray from current starting index
        for j in range(i, len(nums)):

            # Add current element into subarray sum
            curr += nums[j]

            # Check subarray length and divisibility
            if ((j - i) + 1) > 1 and curr % k == 0:
                return True

    # No valid subarray found
    return False   


# Main function execution
if __name__ == "__main__":
    print(main(), "bru")


# Time Complexity: O(n²)
# Space Complexity: O(1)


'''
Theory Explanation (Brute Force):

1. This approach checks every possible subarray.

2. First loop selects the starting index.

3. Second loop expands the subarray.

4. curr stores the sum of current subarray.

5. For every subarray we check:

   -> Length must be at least 2.
   -> Sum must be divisible by k.

6. If both conditions are satisfied:
   Return True.

Important Steps:

-> (j - i) + 1 gives subarray length.
-> curr % k == 0 checks multiple of k.
-> Every possible contiguous subarray is checked.

Key Intuition:

Generate every possible subarray,
calculate its sum,
and check whether it is a multiple of k.
'''



"""========================================Optimal Approach=========================="""


def main():

    # Input array
    nums = [23,2,6,4,7]

    # Divisor value
    k = 6

    # Store remainder and its earliest index
    mapp = {}

    # Handle prefix sum divisible by k
    mapp[0] = -1

    # Store prefix sum
    curr = 0

    # Traverse array
    for i in range(len(nums)):

        # Update prefix sum
        curr += nums[i]

        # Calculate remainder
        rem = curr % k

        # Check if same remainder was seen before
        if rem in mapp:

            # Get earliest index of same remainder
            old_indx = mapp[rem]

            # Check subarray length is at least 2
            if (i - old_indx) > 1:
                return True

        # Store remainder only if seen first time
        else:
            mapp[rem] = i

    # No valid subarray found
    return False   


# Main function execution
if __name__ == "__main__":
    print(main())


# Time Complexity: O(n)
# Space Complexity: O(min(n, k))


'''
Theory Explanation (Optimal Approach):

1. This problem uses Prefix Sum + HashMap.

2. curr stores the prefix sum.

3. For every prefix sum,
   calculate:

   remainder = curr % k

4. Main mathematical idea:

   If two prefix sums have the same remainder,
   then their difference is divisible by k.

Example:

Prefix Sum 1 = 23
23 % 6 = 5

Prefix Sum 2 = 35
35 % 6 = 5

Difference:

35 - 23 = 12

12 % 6 = 0

5. Therefore,
   if the same remainder appears again,
   the subarray between those two indices
   has a sum which is a multiple of k.

6. HashMap stores:

   remainder -> earliest index

7. mapp[0] = -1 is important.

   It handles the case where
   prefix sum itself is divisible by k.

Example:

nums = [2,4]

Prefix sum at index 1 = 6

6 % 6 = 0

mapp already contains:

0 -> -1

Length:

1 - (-1) = 2

So valid subarray is found.

Important Steps:

-> Store remainder, not prefix sum.
-> Store the earliest index of each remainder.
-> Do not update an already existing remainder.
-> Check index difference greater than 1.
-> mapp[0] = -1 handles complete prefix subarrays.

Key Intuition:

Same remainder means
the difference between two prefix sums
is divisible by k.

That difference represents
a contiguous subarray sum.

Prefix Sum + Same Remainder
= Subarray Sum Multiple of K
'''