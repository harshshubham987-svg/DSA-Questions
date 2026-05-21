def first_num(num, n, t):
    if num < n:
        return t
    return first_num(num, n+1, t+n)

num = 5
print(first_num(num, 1, 0))