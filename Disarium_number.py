n = int(input())
t,s = n,n
x = 0
a = 0
while(t):
    t//=10
    x+=1
while(s):
    a+=(s%10)**x
    x-=1
    s//=10
if(a==n):
    print("True")
else:
    print("False")