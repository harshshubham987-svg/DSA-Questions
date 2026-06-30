# 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""============================================ Brute Force Approach ===================================================="""
def merg(num1, num2):
    i = 0
    j = 0

    m = []

    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            m.append(num1[i])
            i+=1
        else:
            m.append(num2[j])
            j += 1
    
    while i < len(num1):
        m.append(num1[i])
        i += 1
    while j < len(num2):
        m.append(num2[j])
        j+= 1

    return m

def main():
    num1 = [1,2]
    num2 = [3,4]

    merg_array = merg(num1, num2)
    
    s = 0
    e = len(merg_array)-1

    ans = (s+e)//2

    if len(merg_array) % 2 != 0:
        print(merg_array[ans])
    
    else:
        r_ans = (merg_array[ans] + merg_array[ans+1])/2
        print(r_ans)

if __name__ == "__main__":
    main()
