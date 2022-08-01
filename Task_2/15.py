# Enter your code here. Read input from STDIN. Print output to STDOUT

A = int(input())
a = set(map(int,input().strip().split(' ')))

B = int(input())
b = set(map(int,input().strip().split(' ')))

res = a.symmetric_difference(b)
print(len(res))