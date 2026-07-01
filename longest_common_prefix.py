'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''

def find_common(strs):
    ans = ""

    base = strs[0]

    for i in strs:
        a = ""
        for j in range (len(i)):
            if j < len(base):
                if base[j] == i[j]:
                    a += i[j]
                else:
                    break
            else:
                break
        base = a
        ans = a

    return ans

def main():
    strs = ["flower","flow","flight"]

    print(find_common(strs))

if __name__ == "__main__":
    main()


    