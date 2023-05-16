import math
p, r, t = map(int,input().split())
ci = p*pow(1+(r/100.0), t)
print("%.2f"%ci)