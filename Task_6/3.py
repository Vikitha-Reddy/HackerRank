import numpy
n,m=map(int,input().split())
lst = []
for i in range(n):
    lst.append(input().split())
a = numpy.array(lst,int)
print(numpy.transpose(a))
print(a.flatten())