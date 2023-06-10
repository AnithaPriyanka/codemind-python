a=input()
x1=0
x2=0
y1=0
y2=0
z1=0
z2=0
for i in a:
    if i=="(":
        x1=x1+1
    if i==")":
        x2=x2+1
    if i=="[":
        y1=y1+1
    if i=="]":
        y2=y2+1
    if i=="{":
        z1=z1+1
    if i=="}":
        z2=z2+1
if x1==x2 and y1==y2 and z1==z2:
    print("True")
else:
    print("False")