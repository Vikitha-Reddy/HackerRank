# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = int(input())
BC = int(input())
AC = math.sqrt(AB**2 + BC**2)
opp = AC/2.0
adj = BC/2.0
res = int(round(math.degrees(math.acos(adj/opp))))
print(str(res)+str('°'))