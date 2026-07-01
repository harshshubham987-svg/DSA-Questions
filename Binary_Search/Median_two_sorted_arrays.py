# 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000


"""============================================ Brute Force Approach ===================================================="""


def merg(num1, num2):
    # Pointer for first array
    i = 0

    # Pointer for second array
    j = 0

    # Store merged array
    m = []

    # Merge both arrays in sorted order
    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            m.append(num1[i])
            i += 1
        else:
            m.append(num2[j])
            j += 1
    
    # Add remaining elements of first array
    while i < len(num1):
        m.append(num1[i])
        i += 1

    # Add remaining elements of second array
    while j < len(num2):
        m.append(num2[j])
        j += 1

    return m


def main():
    # Input arrays
    num1 = [1,2]
    num2 = [3,4]

    # Merge both arrays
    merg_array = merg(num1, num2)
    
    # Start index
    s = 0

    # End index
    e = len(merg_array) - 1

    # Middle index
    ans = (s + e) // 2

    # If array length is odd
    if len(merg_array) % 2 != 0:
        print(merg_array[ans])
    
    # If array length is even
    else:
        r_ans = (merg_array[ans] + merg_array[ans + 1]) / 2
        print(r_ans)


if __name__ == "__main__":
    main()


# Time Complexity: O(m+n)
# Space Complexity: O(m+n)


'''
Theory (Brute Force):

1. Merge both sorted arrays.
2. Find middle element.
3. If odd length:
   return middle.
4. If even length:
   return average of middle two.

Important:
-> Simple and easy.
-> Uses extra space.
'''


'''============================================================ Optimal Approach ========================================================='''


def median(num1, num2):

    # Total length of both arrays
    total = len(num1) + len(num2)

    # Binary search range on first array
    s = 0
    e = len(num1)

    # Store final median
    median = 0

    # Apply binary search
    while s <= e:

        # Partition for first array
        cut1 = (s + e) // 2

        # Left side of first array
        if cut1 == 0:
            left1 = float("-inf")
        else:
            left1 = num1[cut1 - 1]

        # Right side of first array
        if cut1 == len(num1):
            right1 = float("inf")
        else:
            right1 = num1[cut1]

        # Total left partition size
        total_lef = (total + 1) // 2

        # Partition for second array
        cut2 = total_lef - cut1

        # Left side of second array
        if cut2 == 0:
            left2 = float("-inf")
        else:
            left2 = num2[cut2 - 1]
        
        # Right side of second array
        if cut2 == len(num2):
            right2 = float("inf")
        else:
            right2 = num2[cut2]

        # Valid partition found
        if left1 <= right2 and left2 <= right1:

            # Odd total length
            if total % 2 != 0:
                median = max(left1, left2)
                return median
            
            # Even total length
            else:
                max_left = max(left1, left2)
                min_rig = min(right1, right2)

                median = (max_left + min_rig) / 2
                return float(median)

        # Move right
        elif left2 > right1:
            s = cut1 + 1

        # Move left
        elif left1 > right2:
            e = cut1 - 1


def main():
    # Input arrays
    num1 = [1,2]
    num2 = [3,4]

    # Find median
    ans = median(num1, num2)

    # Print answer
    print(ans)


if __name__ == "__main__":
    main()


# Time Complexity: O(log(min(m,n)))
# Space Complexity: O(1)


'''
Theory (Optimal):

1. Use Binary Search on smaller array.

2. Divide both arrays into left and right partitions.

3. Conditions:
   left1 <= right2
   left2 <= right1

4. If valid:
   -> Odd: max(left side)
   -> Even: average of middle two

5. If invalid:
   -> Adjust binary search.

Important:
-> No extra space.
-> Very fast.
-> Harder to understand but interview favorite.

Key Intuition:

We are not merging.
We are directly finding the correct cut point.
That cut point gives median instantly.
'''