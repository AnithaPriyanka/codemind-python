n=int(input())
c=0
d=0
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in a:
    c+=i
for i in b:
    d+=i
if c>d:
    print(0)
else:
    print(d-c)