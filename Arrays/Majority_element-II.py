'''
229. Majority Element II

Given an integer array nums,
return all elements that appear
more than ⌊n / 3⌋ times.

Follow up:
Solve in O(n) time
and O(1) extra space.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]
'''

# Solution

def main():

    # Input array
    nums = [1,2]

    # First candidate
    candidate1 = 0
    count1 = 0

    # Second candidate
    candidate2 = 0
    count2 = 0

    # First pass:
    # Find possible majority candidates
    for n in nums:

        # Increase count if first candidate matches
        if n == candidate1:
            count1 += 1

        # Increase count if second candidate matches
        elif n == candidate2:
            count2 += 1

        # Select first candidate
        elif count1 == 0:
            candidate1 = n
            count1 = 1

        # Select second candidate
        elif count2 == 0:
            candidate2 = n
            count2 = 1

        # Cancel both counts
        else:
            count1 -= 1
            count2 -= 1

    # Verify actual frequencies
    c1 = 0
    c2 = 0

    for n in nums:

        if n == candidate1:
            c1 += 1

        elif n == candidate2:
            c2 += 1

    # Store final answer
    ans = []

    # Check first candidate
    if c1 > (len(nums) / 3):
        ans.append(candidate1)

    # Check second candidate
    if c2 > (len(nums) / 3):
        ans.append(candidate2)

    return ans


# Print final answer
print(main())

# Time Complexity: O(n)
# Space Complexity: O(1)

'''
Theory Explanation:

1. This problem uses Boyer-Moore Voting Algorithm.

2. Observation:

   More than n/3 frequency means
   there can be at most 2 majority elements.

3. First Pass:

   Find two possible candidates.

4. Rules:

   -> If number matches candidate,
      increase its count.

   -> If candidate count becomes zero,
      replace it with current number.

   -> Otherwise,
      decrease both counts.

5. Second Pass:

   Candidates are only possible answers,
   so count their actual frequencies.

6. Add candidates to answer
   only if frequency > n/3.

Important Steps:

-> Maximum two majority elements.
-> First pass finds candidates only.
-> Second pass verifies candidates.
-> Boyer-Moore works in O(1) extra space.

Key Intuition:

Different numbers cancel each other.
Only the elements occurring
more than n/3 times
can survive as final candidates.
'''