# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def normal_dist(mean, sd, time):
    p = 0.5*(1 + math.erf((time-mean)/(sd*math.sqrt(2.0))));
    return p;

mean,sd = list(map(float, input().split(" ")))
time = float(input())
t_1,t_2 = list(map(float, input().split(" ")))
p1 = normal_dist(mean, sd, time);
p2 = normal_dist(mean, sd, t_2) - normal_dist(mean, sd, t_1);
print(round(p1,3))
print(round(p2,3))