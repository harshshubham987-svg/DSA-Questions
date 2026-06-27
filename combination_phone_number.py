'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = "2"
Output: ["a","b","c"]
'''

# Solution:

def comb(dig, indx, curr, ans):

    # Store digit to letter mapping
    phone = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqr",
        "8":"tuv",
        "9":"wxyz"
    }

    # Base case:
    # If current combination length becomes equal to digits length
    if len(curr) == len(dig):
        ans.append("".join(curr))
        return

    # Get current digit
    cur_dig = dig[indx]

    # Traverse all characters mapped to current digit
    for ch in phone[cur_dig]:

        # Take current character
        curr.append(ch)

        # Move to next digit
        comb(dig, indx + 1, curr, ans)

        # Backtrack by removing last character
        curr.pop()


def main():
    # Input digits
    digit = "23"

    # Store all combinations
    ans = []

    # Start recursion
    comb(digit, 0, [], ans)

    # Print final answer
    print(ans)


# Main function execution
if __name__ == "__main__":
    main()

# Time Complexity: O(4^n)
# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses Recursion + Backtracking.

2. Each digit has multiple possible letters.

3. At every digit:
   We try all possible letters.

4. For each letter:
   -> Add it to current combination.
   -> Move to next digit.

5. If current combination length becomes equal
   to total digits length:
   Store the result.

6. Backtracking:
   After recursion,
   remove the last character
   and try the next one.

Important Steps:

-> Use mapping to get letters of current digit.
-> Join list into string before storing.
-> curr.pop() is important for backtracking.
-> Each digit branches into multiple choices.

Key Intuition:

For every digit,
pick one letter,
build the word,
and explore all possibilities.
'''