import math as m
n = int(input())
for i in range(n):
    a, b = sorted(map(int, input().split()))
    if (a+a) < b:
        print(int(m.pow(b, 2)))
    else:
        print(int(m.pow((a+a), 2)))
