import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    rev_arr = numpy.array(arr[::-1],float)
    return rev_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)