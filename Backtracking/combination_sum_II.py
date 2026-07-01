'''
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]
'''

# solution:

def comb_sum(arr, indx, target, curr, ans):

    # If target becomes 0, store current combination
    if target == 0:
        ans.append(curr[:])
        return
    
    # If target becomes negative, stop recursion
    elif target < 0:
        return
    
    # If index goes out of range, stop recursion
    elif indx == len(arr):
        return
    
    # Take current element
    curr.append(arr[indx])

    # Move to next index (element can be used only once)
    comb_sum(arr, indx + 1, target - arr[indx], curr, ans)

    # Backtrack by removing last element
    curr.pop()

    # Skip duplicate elements
    while indx + 1 < len(arr) and arr[indx] == arr[indx + 1]:
        indx += 1
    
    # Skip current element and move forward
    comb_sum(arr, indx + 1, target, curr, ans)


def main():
    # Input array
    arr = [10,1,2,7,6,1,5]

    # Target value
    target = 8

    # Store all valid combinations
    ans = []

    # Sort array for duplicate handling
    arr.sort()

    # Start recursion
    comb_sum(arr, 0, target, [], ans)

    # Print final result
    print(ans)


# Main function execution
if __name__ == "__main__":
    main()

# Time Complexity: O(2^n)
# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses Recursion + Backtracking.

2. At every index, we have two choices:
   -> Take the current element
   -> Skip the current element

3. Difference from Combination Sum I:
   Here each element can only be used once,
   so after taking it, we move to indx + 1.

4. If target becomes 0:
   We found a valid combination.

5. If target becomes negative:
   Stop, because it cannot form target.

6. Sorting is important:
   It places duplicates together.

7. While skipping:
   We skip all duplicate values
   to avoid duplicate combinations.

Important Steps:

-> Sort array before recursion.
-> Use curr[:] to save a copy.
-> Backtracking removes last chosen element.
-> Skip duplicates only in "not take" path.

Key Intuition:

Pick the number once,
move ahead,
and avoid repeating same combination.
'''