# # Enter your code here. Read input from STDIN. Print output to STDOUT
# set_A = set(map(int,input().split()))
# flag = False
# for i in range(int(input())):
#     set_B = set(map(int,input().split()))
#     if len(set_A)>len(set_B):
#         for j in set_B:
#             # print(j)
#             if j in set_A:
#                 flag=True
#             else:
#                 flag=False
#                 break
# print(flag)

def isstrictsuperset(a,b):
    # true if a is a strict superset of b
    return b.issubset(a) and not(a.issubset(b))

a = set(int(x) for x in input().split(' '))
n = int(input())
res = True

for _ in range(n):
    b = set(int(x) for x in input().split(' '))
    res &= isstrictsuperset(a,b)
    
print(res)