'''39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []'''

# solution:

def track_sum(arr, indx, target, current, ans):

    # If target becomes 0, store the current combination
    if target == 0:
        ans.append(current[:])
        return
    
    # If index goes out of range, stop recursion
    elif indx == len(arr):
        return
    
    # If target becomes negative, stop recursion
    elif target < 0:
        return

    # Choose current element
    current.append(arr[indx])

    # Recur with same index (because same element can be reused)
    track_sum(arr, indx, target - arr[indx], current, ans)

    # Backtrack by removing last added element
    current.pop()

    # Skip current element and move to next index
    track_sum(arr, indx + 1, target, current, ans)


def main():
    # Input array
    arr = [2, 3, 6, 7]

    # Target value
    tar = 7

    # Store all valid combinations
    ans = []

    # Start backtracking
    track_sum(arr, 0, tar, [], ans)

    # Print final answer
    print(ans)


# Main function execution
if __name__ == "__main__":
    main()

# Time Complexity: O(2^target)
# Space Complexity: O(target)