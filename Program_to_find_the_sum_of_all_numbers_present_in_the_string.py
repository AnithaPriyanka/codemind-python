n = input()
s=0
for i in range(len(n)):
    if n[i] in "123456789":
        s+=int(n[i])
print(s)