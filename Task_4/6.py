if __name__ == '__main__':
    s = input()
    print(True in list(map(lambda x:x.isalnum(),s)))
    print(True in list(map(lambda x:x.isalpha(),s)))
    print(True in list(map(lambda x:x.isdigit(),s)))
    print(True in list(map(lambda x:x.islower(),s)))
    print(True in list(map(lambda x:x.isupper(),s)))
