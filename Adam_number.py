import math
n = int(input())
s = n*n
rev=0
rev2=0
while(s!=0):
    r=s%10
    rev=rev*10+r
    s=s//10
sq=math.sqrt(rev)
while(sq!=0):
    r2=sq%10
    rev2=rev2*10+r2
    sq=sq//10
if(rev2==n):
    print("True")
else:
    print("False")