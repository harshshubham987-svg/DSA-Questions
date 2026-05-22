def first_num(num):
    if num == 0:
        return num
    return num + first_num(num-1) 

num = 5
print(first_num(num))