s = "abba"
l = 0
max_len = 0

seen = set()

for r in range(len(s)):
    ch = s[r]
    while ch in seen:
        seen.remove(s[l])
        l += 1
    seen.add(ch)
    max_len = max(max_len, r-l+1)

print(max_len)