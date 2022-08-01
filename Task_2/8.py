# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().strip().split(' '))
arr = list(map(int, input().strip().split(' ')))
A = set(map(int, input().strip().split(' ')))
B = set(map(int, input().strip().split(' ')))
count =  0
for i in arr:
    if i in A:
            count += 1
    elif i in B:
            count -= 1
print(count)