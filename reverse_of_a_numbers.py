n = int(input())
rem = 0
while(n>0):
    r = n%10
    rem = rem*10+r
    n = n//10
print(rem)