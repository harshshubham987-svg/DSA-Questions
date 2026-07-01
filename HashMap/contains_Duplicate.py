#----QUESTION 1: Contains Duplicate----

nums = [1, 2, 3, 1]

seen = set()


for num in nums:
    if num in seen:
        print("True")
        break
    seen.add(num)
else:
    print("False")

