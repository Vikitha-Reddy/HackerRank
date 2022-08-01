if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
# arr = list(arr)
res = [*set(arr)]
res.sort(reverse=True)
print(res[1])