a, b = map(int, input().split())
for i in range(1,100):
    a = a * 3
    b = b * 2
    if b < a:
        print(i)
        break