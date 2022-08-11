import numpy
numpy.set_printoptions(legacy='1.13')
arr_A = input().strip().split()
arr_A = numpy.array(arr_A, float)
print(numpy.floor(arr_A))
print(numpy.ceil(arr_A))
print(numpy.rint(arr_A))
