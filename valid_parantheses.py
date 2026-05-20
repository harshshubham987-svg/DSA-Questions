string = "({[]})"

dic = {
    ")" : "(",
    "}" : "{",
    "]" : "["
}

stack = []
valid = True

for i in range(len(string)):
    curr = string[i]

    if curr in dic:
        if stack and dic[curr] == stack[-1]:
            stack.pop()
        else:
            valid = False
            break
    else:
        stack.append(curr)

if valid and len(stack) == 0:
    print("valid parantheses")
else:
    print("InValid Parantheses")
