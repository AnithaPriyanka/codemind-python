import math
a, b = map(int,input().split())
s=0
for i in range(a, b+1):
    sq = math.sqrt(i)
    s=s+sq
print("%.2f"%s)