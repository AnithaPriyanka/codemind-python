def perfect(n):
    s=0;
    for i in range(1,n):
        if n%i==0:
            s += i
    return s==n
n = int(input())
if perfect(n):
    print("True")
else :
    print("False")