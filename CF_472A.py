import math as m
n = int(input())
x = n // 2
y = m.ceil(n/2)
while True:
    if (x % 2 == 0 or x % 3 == 0) and (y % 2 == 0 or y % 3 == 0):
        print(f"{x} {y}")
        break
    else:
        x -= 1
        y += 1
