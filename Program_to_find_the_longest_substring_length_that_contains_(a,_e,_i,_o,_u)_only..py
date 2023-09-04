n = input()
c=0
maxi = 0
for i in n:
    if i in "aeiou":
        c+=1
        maxi=max(c,maxi)
    else:
        c=0
print(maxi)