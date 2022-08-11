import numpy
N,M = map(int,input().split())
A = numpy.array([input().split() for i in range(N)], int)
print(A.mean(axis=1))
print(A.var(axis=0))
print(numpy.round(numpy.std(A), 11))
