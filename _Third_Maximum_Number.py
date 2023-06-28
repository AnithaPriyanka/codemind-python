n = int(input())
l = list(map(int,input().split()))
l = set(l)
if len(l)==1:
    print(max(l))
elif len(l)==2:
    print(max(l))
elif len(l)==3:
    print(min(l))
else:
    l.remove(max(l))
    l.remove(max(l))
    print(max(l))