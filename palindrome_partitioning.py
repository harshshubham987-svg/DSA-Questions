'''
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]
'''

# solution:

def palin_part(s, start, curr, ans):

    # If start reaches end of string,
    # store current partition
    if start == len(s):
        ans.append(curr[:])
        return

    # Try all possible substrings starting from "start"
    for end in range(start, len(s)):

        # Create substring from start to end
        sub = s[start:end+1]

        # Check if substring is palindrome
        if sub == sub[::-1]:

            # Add palindrome substring
            curr.append(sub)

            # Recur for remaining string
            palin_part(s, end+1, curr, ans)

            # Backtrack by removing last substring
            curr.pop()


def main():
    # Input string
    s = "aab"

    # Store all palindrome partitions
    ans = []

    # Start recursion
    palin_part(s, 0, [], ans)

    # Print final answer
    print(ans)


# Main function execution
if __name__ == "__main__":
    main()

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses Recursion + Backtracking.

2. At every index:
   We try all possible substrings.

3. For each substring:
   -> Check if it is a palindrome.
   -> If yes, take it.
   -> Solve remaining part.

4. If start reaches end of string:
   It means one valid partition is formed.

5. Backtracking:
   After recursion,
   remove the last chosen substring
   and try another.

Important Steps:

-> Loop helps generate all possible cuts.
-> Palindrome check is important before recursion.
-> curr[:] stores a copy of current partition.
-> Backtracking restores previous state.

Key Intuition:

Cut the string at every possible point,
but only continue if the current piece is palindrome.
'''