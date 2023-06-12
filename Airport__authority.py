n = int(input())
c = 0
lst = []
for i in range(1, n+1):
    a = int(input())
    lst.append(a)
x = int(input())
for i in lst:
    if i<=x:
        c=c+1
    else:
        c=c+2
print(c)