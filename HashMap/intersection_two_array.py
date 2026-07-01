'''
350. Intersection of Two Arrays II - problem description

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays.
The result can be returned in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9] (order may vary)

'''

# solution implementation

# Example input arrays
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

# Build a frequency map for elements in nums1
mapp = {}
for i in nums1:
    if i in mapp:
        mapp[i] += 1  # increment count if already seen
    else:
        mapp[i] = 1   # initialize count

# Collect intersection elements based on the frequency map
new_lis = []
for j in nums2:
    if j in mapp and mapp[j] > 0:
        mapp[j] -= 1   # decrement count to avoid over-counting
        new_lis.append(j)  # add to result list
    else:
        continue  # skip if element not in map or count exhausted

print(new_lis)  # Output the intersection list

# Time Complexity: O(m + n) where m and n are lengths of nums1 and nums2
# Space Complexity: O(min(m, n)) for the frequency map