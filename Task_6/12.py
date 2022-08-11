import numpy
n = int(input())
A = numpy.array([input().split() for i in range(n)],int)
B = numpy.array([input().split() for i in range(n)],int)
result = numpy.dot(A,B)
print(result)
