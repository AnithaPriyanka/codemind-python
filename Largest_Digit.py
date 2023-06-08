n = int(input())
s = str(n)
gd = int(s[0])
for i in range(1, len(s)):
    r = int(s[i])
    if r > gd:
        gd = r
print(gd)