# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
m = set(map(int, input().split(' ')))

N = int(input())
n = set(map(int, input().split(' ')))

a = m.difference(n)
b = n.difference(m)

c = list(a.union(b))
c.sort()
for i in c:
    print(i)