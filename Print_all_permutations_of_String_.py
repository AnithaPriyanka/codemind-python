from itertools import permutations
n=input()
lst=list(permutations(range(0,len(n))))
for i in lst:
    for j in i:
        print(n[j],end="")
    print()