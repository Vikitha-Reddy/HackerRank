if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        # print(name) Krishna
        # print(line) ['67', '68', '69']
        # print(scores) [67.0, 68.0, 69.0]
        # print(student_marks) {'Krishna': [67.0, 68.0, 69.0]}
    query_name = input()
    sum = 0
    avg = 0
    for key,val in student_marks.items():
        if key==query_name:
            for i in val:
                sum = sum+i
                avg = sum/3
    print(format(avg,'.2f'))