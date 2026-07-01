def fact(num,n,prod):
    if num < n:
        return prod
    return fact(num,n+1,prod*n)

num = 5
print(fact(num,1,1))