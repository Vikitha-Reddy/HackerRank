# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
lst = list(map(int,input().split(' ')))
captain_room = lst[0]
# print(lst)
counter = dict(Counter(lst))
for k,v in counter.items():
    if v == 1:
        captain_room = k
        break
print(captain_room)