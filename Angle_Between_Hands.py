x = input()
x = x.split(":")
h = int(x[0])
m = int(x[1])
a = abs((30*h)-(11/2)*m)
if a<180:
    print(a)
else:
    print(360-a)