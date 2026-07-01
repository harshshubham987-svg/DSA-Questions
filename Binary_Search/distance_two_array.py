'''
1385. Find the Distance Value Between Two Arrays

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

 

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2
Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1
'''
'''============================================Brute force approach=================================='''
# arr1 = [2,1,100,3]
# arr2 = [-5,-2,10,-3,7]
# d = 6

# count = 0
# yes = 0

# j = 0
# i = 0

# while i < len(arr1):

#     if j < len(arr2):
#         num = arr1[i] - arr2[j]
#         num = abs(num)
#         print(f"j :- {j} , num :- {num}")

#         if num > d:
#             yes += 1
#             j += 1
#         else:
#             j = 0
#             i+= 1
#             yes = 0
    
#     else:
#         if yes == len(arr2):
#             count += 1
#         yes = 0
#         j = 0
#         i += 1
        
# print(count)

'''===========================================================Optimal Approach==================================================='''


def binary_search(arr, target):

    # Start pointer
    s = 0
    
    # End pointer
    e = len(arr) - 1

    # Default answer (if no valid index found)
    ans = len(arr)

    # Apply binary search
    while s <= e:

        # Find middle index
        mid = (s + e) // 2

        # If current value is greater than or equal to target
        if arr[mid] >= target:
            
            # Store current index as possible answer
            ans = mid
            
            # Search on left side for smaller valid index
            e = mid - 1
        
        # Otherwise move to right side
        else:
            s = mid + 1
    
    # Return found index
    return ans


def main():
    
    # First array
    arr1 = [2, 1, 100, 3]
    
    # Second array
    arr2 = [-5, -2, 10, -3, 7]
    
    # Distance value
    d = 6

    # Sort second array for binary search
    arr2.sort()

    # Count valid elements
    count = 0

    # Traverse through arr1
    for num in arr1:
        
        # Find first element in arr2 >= (num-d)
        n = binary_search(arr2, num - d)

        # Check if no element exists in valid range [num-d, num+d]
        if n == len(arr2) or arr2[n] > num + d:
            count += 1
    
    # Return total count
    return count


# Main function execution
if __name__ == "__main__":
    print(main())

# Time Complexity: O(n log m + m log m)
# Space Complexity: O(1)