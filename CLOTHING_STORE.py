n = int(input())
l = list(map(int,input().split()))
l.sort()
c = 0
b = set(l)
for i in b:
    if l.count(i)>1:
        c += l.count(i)//2
print(c)