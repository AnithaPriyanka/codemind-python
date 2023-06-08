import math
n = int(input())
arr = list(map(int,input().split()))
res = math.gcd(*arr)
print(res)