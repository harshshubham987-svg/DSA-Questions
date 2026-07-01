arr = [1,2,2,2,3]
tar = 3

low = 0
hig = len(arr)-1

ans = -1

while low <= hig:
    mid = (low+hig)//2

    if arr[mid] == tar:
        low = mid +1
        ans = mid
    elif arr[mid] > tar:
        hig = mid -1
    else:
        low = mid +1

print(ans)