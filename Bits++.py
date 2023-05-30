t = int(input())
c=0
for i in range(t):
    n = input()
    if '++' in n:
        c += 1
    elif '--' in n:
        c -= 1
print(c)