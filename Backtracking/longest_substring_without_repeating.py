'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.'''

def main():

    # Input string
    s = "abcabcbb"

    # Store unique characters in current window
    sets = set()

    # Left pointer of sliding window
    lef = 0

    # Right pointer of sliding window
    rig = 0

    # Store maximum length of substring
    max_len = 0
    
    # Traverse string using right pointer
    while rig <= len(s) - 1:

        # Current character
        ch = s[rig]

        # If duplicate exists, shrink window from left
        while ch in sets:
            sets.remove(s[lef])
            lef += 1

        # Add current character into set
        sets.add(ch)

        # Calculate current window length
        curr_len = (rig - lef) + 1

        # Update maximum length
        max_len = max(max_len, curr_len)

        # Expand window
        rig += 1
        
    # Return final answer
    return max_len


# Print final result
if __name__ == "__main__":
    print(main())

# Time Complexity: O(n)
# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses Sliding Window + Set.

2. Goal:
   Find longest substring without repeating characters.

3. Window is defined by:
   lef → start
   rig → end

4. Expand window by moving rig.

5. If duplicate character appears:
   Shrink window from lef
   until duplicate is removed.

6. Set helps:
   -> Fast lookup O(1)
   -> Check if character already exists.

Important Steps:

-> Expand with rig.
-> Shrink with lef when duplicate found.
-> Always maintain unique characters in set.
-> Update max length after valid window.

Key Intuition:

Maintain a window
where all characters are unique,
and keep growing it as much as possible.
'''



