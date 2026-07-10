'''
77. Combinations

Given two integers n and k,
return all possible combinations
of k numbers chosen from [1, n].

Example 1:

Input: n = 4, k = 2
Output:
[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Example 2:

Input: n = 1, k = 1
Output:
[[1]]
'''

# Solution

def dfs(n, s, k, path, ans):

    # If required combination size is reached,
    # store the current combination
    if len(path) == k:
        ans.append(path[:])
        return

    # Try every possible number
    # starting from current value
    for i in range(s, n + 1):

        # Choose current number
        path.append(i)

        # Recur for next available number
        dfs(n, i + 1, k, path, ans)

        # Backtrack by removing last number
        path.pop()


def main():

    # Maximum number
    n = 4

    # Required combination size
    k = 2

    # Store all combinations
    ans = []

    # Start recursion from number 1
    dfs(n, 1, k, [], ans)

    # Print final answer
    print(ans)


# Main function execution
if __name__ == "__main__":
    main()

# Time Complexity: O(C(n, k) × k)
# Space Complexity: O(k)

'''
Theory Explanation:

1. This problem uses Backtracking.

2. Goal:
   Choose exactly k numbers
   from the range [1, n].

3. At every step:
   Select one number
   and move forward.

4. After selecting a number:
   Next recursion starts from
   the next number (i + 1).

5. This prevents duplicate combinations.

6. When path size becomes k:
   Store the current combination.

7. Backtrack:
   Remove the last selected number
   and try another choice.

Important Steps:

-> Start from current number s.
-> Move forward only (i + 1).
-> Use path[:] to store a copy.
-> Backtracking restores previous state.

Key Intuition:

Choose one number,
move only forward,
and build combinations
without repeating previous numbers.
'''