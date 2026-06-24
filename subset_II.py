''''
90. Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

''''

# solution

def subset(arr, indx, curr, ans):

    # If index reaches the end, store the current subset
    if indx == len(arr):
        ans.append(curr[:])
        return

    # Take the current element
    curr.append(arr[indx])

    # Move to next index after taking the element
    subset(arr, indx + 1, curr, ans)

    # Backtrack by removing the last element
    curr.pop()

    # Skip duplicate elements
    while indx + 1 < len(arr) and arr[indx] == arr[indx + 1]:
        indx += 1
    
    # Move to next unique element without taking current
    subset(arr, indx + 1, curr, ans)


def main():
    # Input array
    nums = [4,4,4,1,4]

    # Store all subsets
    ans = []

    # Sort array to handle duplicates together
    nums.sort()

    # Start recursion
    subset(nums, 0, [], ans)

    # Sort subsets by length
    ans.sort(key=len)

    # Print final answer
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
   -> Take the element
   -> Skip the element

3. "Take" means:
   Add current element into current subset
   and move forward.

4. "Backtrack" means:
   Remove the last added element
   so we can explore the next possible choice.

5. "Skip" means:
   Ignore current element and move forward.

6. Since duplicates exist,
   sorting is important so all duplicate values stay together.

7. While skipping:
   we move over all duplicate values
   to avoid generating duplicate subsets.

Important Steps:

-> Sorting is mandatory for duplicate handling.
-> Always copy the current subset using curr[:].
-> Backtracking keeps memory optimized.
-> While loop is the key for avoiding duplicate subsets.
'''