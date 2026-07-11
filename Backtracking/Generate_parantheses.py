'''
22. Generate Parentheses

Given n pairs of parentheses,
generate all combinations of
well-formed parentheses.

Example 1:

Input:
n = 3

Output:
["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input:
n = 1

Output:
["()"]
'''

# Solution

def dfs(n, ans, ob, cb, s):

    # If all opening and closing brackets are used,
    # store the valid parentheses combination
    if ob == cb and len(s) == (n * 2):
        ans.append(s)
        return

    # Add opening bracket if limit is not reached
    if ob < n:
        dfs(n, ans, ob + 1, cb, s + "(")

    # Add closing bracket only if
    # opening brackets are greater than closing brackets
    if ob > cb:
        dfs(n, ans, ob, cb + 1, s + ")")


def main():

    # Number of parentheses pairs
    n = 3

    # Store all valid parentheses combinations
    ans = []

    # Start recursion with zero opening and closing brackets
    dfs(n, ans, 0, 0, "")

    # Print final answer
    print(ans)


# Main function execution
main()

# Time Complexity: O(4^n / √n)
# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses Recursion + Backtracking.

2. We track two values:

   ob -> Number of opening brackets used.
   cb -> Number of closing brackets used.

3. Opening bracket '(' can be added when:

   ob < n

   Because we can use only n opening brackets.

4. Closing bracket ')' can be added when:

   ob > cb

   This ensures that a closing bracket
   is never added before a matching opening bracket.

5. Base Case:

   When string length becomes 2 * n
   and opening and closing counts are equal,
   one valid combination is found.

6. Unlike list backtracking,
   we do not need pop() here.

   Strings are immutable in Python,
   so s + "(" and s + ")"
   create new strings for recursive calls.

Important Steps:

-> Opening brackets cannot exceed n.
-> Closing brackets cannot exceed opening brackets.
-> Every valid answer has length 2 * n.
-> ob > cb prevents invalid parentheses.

Key Intuition:

Add '(' whenever it is available.

Add ')' only when
there is an unmatched '(' before it.

This way,
we generate only valid parentheses
instead of generating all combinations
and checking them later.
'''