import numpy
P,N,M= map(int, input().split())
a = numpy.array([input().split() for _ in range(P)],int)
b = numpy.array([input().split() for _ in range(N)],int)
print(numpy.concatenate((a,b), axis = 0))
