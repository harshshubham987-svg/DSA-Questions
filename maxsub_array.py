arr = [-2,1,-3,4,-1,2,1,-5,4]
k = 4

windsum = sum(arr[:k])      # first window sum
max_sum = windsum

for i in range(3,len(arr)):     # loop from k to len(arr)
    windsum = windsum - arr[i-k] + arr[i]       #slide window
    max_sum = max(windsum, max_sum)     # update max_sum

print(max_sum)