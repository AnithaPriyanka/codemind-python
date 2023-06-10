a=input()
a=a.split(":")
h=int(a[0])
m=int(a[1])
if h>12 and h<24:
    if h-12<=9:
        print("0"+str(h-12)+":"+a[1]+" "+"PM")
    else:
        print(str(h-12)+":"+a[1]+" "+"PM")
if h>0 and h<12:
    print(a[0]+":"+a[1]+" "+"AM")
if h==0:
    print("12:00 AM")
if h==12:
    print("12:00 PM")