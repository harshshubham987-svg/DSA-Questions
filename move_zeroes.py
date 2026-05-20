arr = [0,1,0,3,12]

slow = 0

for r in range(len(arr)):
    if arr[r] !=0:
        arr[slow], arr[r] = arr[r], arr[slow]
        slow += 1

print(arr)