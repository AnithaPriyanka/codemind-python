n=input()
a=""
b=""
c=0
for i in n:
    if i in "abcdefghijklmnopqrstuvwxyz":
        a=a+i
a=a[::-1]
for i in range(len(n)):
    if n[i] not in "abcdefghijklmnopqrstuvwxyz":
        b=b+n[i]
    else:
        b=b+a[c]
        c=c+1
print(b)