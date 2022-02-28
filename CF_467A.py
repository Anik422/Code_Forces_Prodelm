n = int(input())
count = 0
for i in range(n):
    x, y = map(int, input().split())
    z = x + 2
    if z <= y:
        count += 1
    else:
        pass
print(count)
