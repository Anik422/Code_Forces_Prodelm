x, y = map(int, input().split())
count = 1
while x * count % 10 != 0 and x * count % 10 != y:
    count += 1
print(count)