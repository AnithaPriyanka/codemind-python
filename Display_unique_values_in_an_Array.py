n = int(input())
l = list(map(int,input().split()))
arr = []
for i in l:
    if l.count(i)==1:
        arr.append(i)
if len(arr)!=0:
    print(*arr)
else:
    print(-1)