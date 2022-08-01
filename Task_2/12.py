e = input()
el = set(map(int,input().split()))
f = input()
fl = set(map(int,input().split()))

u = el.union(fl)

# print(u)

print(len(u))