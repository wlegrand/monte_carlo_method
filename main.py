import math
import random

n = int(input())
R = 1
count = 0

for i in range(0, n):
    ax = 2 * random.uniform(0, 1)
    ay = 2 * random.uniform(0, 1)

    D2 = (ax - R) ** 2 + (ay - R) ** 2
    D = math.sqrt(D2)
    if D <= R:
        count = count + 1

p1 = 4 * count / n

print(p1)
