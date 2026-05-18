#---QUESTION 2: Valid Anagram-----

s = "listen"
t = "silent"

s_len = len(s)
t_len = len(t)

dic = {}

for i in range(s_len):
    c = s[i]
    if c in dic:
        dic[c] += 1

    dic[c] = 1

for j in range(t_len):
    c = t[j]
    if c in dic:
        dic[c] -= 1
    
result = False
for i in dic:
    if dic[i] != 0:
        result = False
        break
    else:
        result = True

if (result):
    print("True")
else:
    print("False")

print(dic)