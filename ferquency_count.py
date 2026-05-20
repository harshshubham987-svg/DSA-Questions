string = "Harsh"

dic = {}

for i in range(len(string)):
    curr = string[i].lower()
    if curr in dic:
        dic[curr] += 1
    else:
        dic[curr] = 1

print(dic)