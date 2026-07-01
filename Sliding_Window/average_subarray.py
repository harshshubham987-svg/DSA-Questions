arr = [1,3,2,6,-1,4,1,8,2]
k = 5
lis = []
windo_sum = sum(arr[:k])
windo_avg = windo_sum/k
lis.append(windo_avg)

for i in range(k, len(arr)):
    windo_sum = windo_sum - arr[i-k] + arr[i]
    avg = windo_sum / k
    lis.append(avg)

print(lis)