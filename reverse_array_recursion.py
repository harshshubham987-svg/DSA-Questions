def reverse(num,s,e):
    if s >= e:
        return num
    
    #swapping:
    num[s], num[e] = num[e], num[s]

    return reverse(num, s+1, e-1)

num = [1,2,3,4,5]
start = 0
end = len(num)-1
print(reverse(num,start,end))