arr = [1,1,2,2,3,3,4]

slow = 0

for r in range(1,len(arr)):
    if arr[r] != arr[r-1]:
        slow += 1
        arr[slow] = arr[r]

print(arr[:slow+1])
    