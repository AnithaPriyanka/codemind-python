import math
t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    l=math.lcm(a,b)
    x=((n//a)+(n//b)-(n//l)*2)
    if x>=k:
        print("Win")
    else:
        print("Lose")