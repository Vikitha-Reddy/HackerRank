import numpy
n,m = map(int, input().split())
arr = numpy.array([input().split() for i in range(n)], int)
min_ax1 = numpy.min(arr,axis=1)
print(max(min_ax1))
