# Enter your code here. Read input from STDIN. Print output to STDOUT
# 100
# 500
# 80
# .95
# 1.96
import math
size=int(input())
mean=float(input())
sd=float(input())
range=float(input())
z=float(input())
sd = sd/math.sqrt(size)
A = mean - z*sd
B = mean + z*sd
print(round(A,2))
print(round(B,2))