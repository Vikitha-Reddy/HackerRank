# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    A = int(input())
    setA = set(map(int,input().split()))
    B = int(input())
    setB = set(map(int,input().split()))
    if len(setA-setB)==0:
        print('True')
    else:
        print('False')