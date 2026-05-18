# brute force approach

nums = [1,3,-1,-3,5,3,6,7]
k = 3

lis = []

for i in range(len(nums)):
    if k+i <= len(nums):
        
        max_num = max(nums[i:k+i])
        lis.append(max_num)
        
    else:
       break

print(lis)