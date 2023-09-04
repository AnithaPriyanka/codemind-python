for i in range(int(input())):
    n=input()
    a=n[0]
    b=n[0]
    for i in range(1,len(n)):
        if a!=n[i]:
            a=n[i]
            b+=n[i]
    print(len(n)-len(b))