# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def clt(mean, sd, score):
    p = 0.5*(1 + math.erf((score-mean)/(sd*math.sqrt(2.0))));
    return p;
max_wt = float(input())
no_of_boxes = int(input())
mean = float(input())
sd = float(input())
mean = mean*no_of_boxes
sd = sd*math.sqrt(no_of_boxes)
print(round(clt(mean,sd,max_wt),4))