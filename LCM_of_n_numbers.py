import math
n = int(input())
lst = list(map(int,input().split()))
res = math.lcm(*lst)
print(res)