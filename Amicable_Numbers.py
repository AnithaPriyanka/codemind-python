def proper_divisor(n):
    s=0
    for i in range(1, n):
        if n%i==0:
            s=s+i
    return s
        
def amicable(n):
    sn=proper_divisor(n)
    ssn=proper_divisor(sn)
    return n==ssn and n!=sn
    
n=int(input())
if amicable(n):
    print("Amicable")
else:
    print("Not Amicable")