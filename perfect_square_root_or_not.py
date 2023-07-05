import math
n = int(input())
sq = math.sqrt(n)
if sq.is_integer():
    print("True")
else:
    print("False")