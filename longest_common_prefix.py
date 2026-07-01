'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
'''

# Solution:

def find_common(strs):

    # Store final common prefix
    ans = ""

    # Take first string as base reference
    base = strs[0]

    # Traverse all strings
    for i in strs:

        # Temporary string to store matching prefix
        a = ""

        # Compare characters one by one
        for j in range(len(i)):

            # Check index is valid in base
            if j < len(base):

                # If characters match
                if base[j] == i[j]:
                    a += i[j]
                
                # Stop if mismatch found
                else:
                    break
            
            # Stop if base length ends
            else:
                break

        # Update base with current common prefix
        base = a

        # Update answer
        ans = a

    return ans


def main():
    # Input array of strings
    strs = ["flower","flow","flight"]

    # Print final common prefix
    print(find_common(strs))


# Main function execution
if __name__ == "__main__":
    main()

# Time Complexity: O(n * m)
# Space Complexity: O(m)

'''
Theory Explanation:

1. This problem finds the common starting characters
   among all strings.

2. Idea:
   -> Take first string as base.
   -> Compare it with every other string.

3. For each string:
   Check character by character.

4. If characters match:
   Add to temporary prefix.

5. If mismatch happens:
   Stop.

6. Update base with new common prefix.

7. Continue until all strings are checked.

Important Steps:

-> First string acts as initial prefix.
-> Prefix keeps shrinking if mismatch happens.
-> If no match, prefix becomes empty.
-> Final base is the answer.

Key Intuition:

Keep reducing the prefix
until it matches all strings.
'''