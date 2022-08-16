# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def normal_dist(mean, sd, score):
    p = 0.5*(1 + math.erf((score-mean)/(sd*math.sqrt(2.0))));
    return p*100;

mean,sd = list(map(float, input().split(" ")))
score_1 = float(input())
score_2 = float(input())
p1 = float(100)-normal_dist(mean, sd, score_1);
p2 = float(100)-normal_dist(mean, sd, score_2);
p3 = normal_dist(mean, sd, score_2);
print(round(p1,2))
print(round(p2,2))
print(round(p3,2))