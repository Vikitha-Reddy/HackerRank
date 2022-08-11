import numpy
n,m = map(int,input().split())
arr = numpy.array([input().split() for i in range(n)],int)
# print(arr)
sum_arr = numpy.sum(arr, axis=0)
print(numpy.prod(sum_arr,axis=0))
