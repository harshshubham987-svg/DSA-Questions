'''
374. Guess Number Higher or Lower
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
'''

Solution:

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize the search bounds
        s = 1  # start of the range
        e = n  # end of the range
        # Perform binary search until the bounds cross
        while s <= e:
            mid = (s+e)//2  # compute midpoint
            # Use the guess API to compare the midpoint with the target
            if guess(mid) == 0:
                return mid  # correct guess
            elif guess(mid) == -1:
                e = mid -1  # target is lower, adjust upper bound
            else:
                s = mid+1  # target is higher, adjust lower bound
        # If not found (should not happen with valid input)
        return -1

# Time Complexity: O(log n) – binary search halves the interval each iteration
# Space Complexity: O(1) – only constant extra variables used
