'''
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
'''

# solution:

def permu(arr, use, curr, ans):

    # If current permutation size becomes equal to array size
    if len(arr) == len(curr):
        
        # Store the complete permutation
        ans.append(curr[:])
        return
    
    # Traverse through all elements
    for i in range(len(arr)):

        # Skip if element is already used
        if use[i]:
            continue
        
        else:
            # Take current element
            curr.append(arr[i])

            # Mark current element as used
            use[i] = True

            # Recur for next position
            permu(arr, use, curr, ans)
        
            # Backtrack by removing last element
            curr.pop()

            # Mark current element as unused
            use[i] = False


def main():
    # Input array
    arr = [1,2,3]

    # Store all permutations
    ans = []

    # Track used elements
    use = []

    # Initialize all elements as unused
    for i in range(len(arr)):
        use.append(False)

    # Start recursion
    permu(arr, use, [], ans)

    # Print final permutations
    print(ans)


# Main function execution
if __name__ == "__main__":
    main()

# Time Complexity: O(n × n!)
# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses Recursion + Backtracking.

2. At every step:
   We try placing each unused element
   into the current permutation.

3. "use" array helps to track:
   which elements are already taken.

4. If an element is already used:
   skip it.

5. If not used:
   -> Take it
   -> Mark it as used
   -> Recur for next position

6. After recursion:
   Backtrack by:
   -> Removing the element
   -> Marking it unused

7. This allows trying all possible arrangements.

Important Steps:

-> use[] prevents duplicate usage in one permutation.
-> curr[:] is important for storing a copy.
-> Backtracking restores the previous state.
-> Total permutations of n elements = n!

Key Intuition:

Pick one element at a time,
fix it,
solve for remaining,
then backtrack and try another.
'''