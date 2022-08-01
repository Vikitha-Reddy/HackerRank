def average(array):
    # your code goes here
    arr = list(set(array))
    l = len(arr)
    sum_1 = sum(arr)
    avg = sum_1/l
    return avg