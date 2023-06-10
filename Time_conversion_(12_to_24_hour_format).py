a=input()
a=a.split(":")
h=int(a[0])
x=a[1].split()
m=int(x[0])
t=x[1]
if t=="PM":
    if h>=1 and h<12:
        print(str(12+h)+":"+x[0])
if h==12:
    if t=="AM":
        print("00:00")
    else:
        print("12:00")
if t=="AM":
    if h>=1 and h<12:
        print(a[0]+":"+x[0])