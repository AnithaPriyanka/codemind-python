n = int(input())
lst = list(map(int,input().split()))
a = 0
b = 0
for i in range(n):
    if i%2 == 0:
        a += lst[i]
    else:
        b += lst[i]
if abs(a-b)%4 == 0:
    print('X')
else:
    print('Y')