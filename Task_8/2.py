# Enter your code here. Read input from STDIN. Print output to STDOUT
def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

def_pist, size  = list(map(float, input().split(" ")))
p =def_pist/100
size =int(size)

print(round(sum([b(i, size, p) for i in range(size) if i<3]), 3))
print(round(sum([b(i, size, p) for i in range(size) if i>1]), 3))