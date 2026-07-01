'''
520. Detect Capital

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.

Example 1:

Input: word = "USA"
Output: true

Example 2:

Input: word = "FlaG"
Output: false
'''

# Input word
word = "usa"

# Check all valid capital conditions
if word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()):
    print("True")
else:
    print("False")

# Time Complexity: O(n)
# Space Complexity: O(1)

'''
Theory Explanation:

1. This problem checks 3 valid cases.

Case 1:
All characters are uppercase.
Example: "USA"

Case 2:
All characters are lowercase.
Example: "leetcode"

Case 3:
First character is uppercase
and all remaining characters are lowercase.
Example: "Google"

2. We use built-in functions:

-> isupper() → checks if all are uppercase.
-> islower() → checks if all are lowercase.

3. For third case:
   word[0].isupper()
   and
   word[1:].islower()

Important Steps:

-> Check all 3 cases.
-> If any one is true, answer is True.
-> Otherwise False.

Key Intuition:

Valid capital usage follows fixed patterns,
so we directly verify those patterns.
'''

