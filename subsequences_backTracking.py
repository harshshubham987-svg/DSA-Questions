'''
Problem: Generate All Subsequences

Problem Statement

Given an integer array nums, return all possible subsequences of the array.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [1,2,3]

Output:
[
 [],
 [1],
 [2],
 [3],
 [1,2],
 [1,3],
 [2,3],
 [1,2,3]
]

Example 2:
Input: nums = [0]

Output:
[
 [],
 [0]
]

'''

# solution :- 

def back_track(arr, indx, current, ans):

    if indx == len(arr):
        ans.append(current[:])
        return
    
    # Take 
    current.append(arr[indx])
    back_track(arr, indx+1, current, ans)
    current.pop()

    #skip
    back_track(arr, indx+1, current, ans)


def main():
    arr = [1,2,3]
    ans = []

    #calling back_track() function

    back_track(arr, 0, [], ans)

    ans.sort(key=len)
    
    print(ans)

# calling main function

if __name__ == "__main__":
    main()


'''
Pattern: Backtracking (Take / Not Take)
Time Complexity: O(2^n)
Space Complexity: O(n)

'''