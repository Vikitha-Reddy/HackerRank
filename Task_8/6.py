# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def clt(mean, sd, score):
    p = 0.5*(1 + math.erf((score-mean)/(sd*math.sqrt(2.0))));
    return p;
tick_left = int(input())
students = int(input())
mean = float(input())
sd = float(input())
mean = mean*students
sd = sd*math.sqrt(students)
print(round(clt(mean,sd,tick_left),4))