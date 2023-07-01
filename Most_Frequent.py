n = int(input())
lst = list(map(int,input().split()))
a = max(set(lst),key=lst.count)
print(a)