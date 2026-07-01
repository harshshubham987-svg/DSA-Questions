arr = [2,1,5,2,3,2]
target = 7

left = 0
windo_sum = 0
min_sum = float('inf')

for right in range(len(arr)):
    windo_sum += arr[right]

    while windo_sum >= target:
        curr_len = right - left + 1
        min_sum = min(min_sum, curr_len)
        windo_sum -= arr[left]
        left += 1

print(min_sum)