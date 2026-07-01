string = "abbaca"

stack = []

for i in range(len(string)):
    curr = string[i]
    if stack and curr == stack[-1]:
        stack.pop()
    else:
        stack.append(curr)
    
print("".join(stack))