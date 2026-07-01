#----QUESTION 3: Two Sum----

nums = [2, 6, 11, 7, 15]
target = 9

dic = {}

for i in range(len(nums)):
    first = nums[i]
    secound = target - first

    if secound in dic:
        print(nums[dic[secound]],nums[i])
        break
    
    dic[first] = i
