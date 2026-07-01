def palindrome(s,f,l):
    if f >= l:
        return True
    
    elif s[f] == s[l]:
        return palindrome(s,f+1,l-1)
    else:
        return False

string = "madam"
start = 0
last = len(string)-1
print(palindrome(string,start,last))