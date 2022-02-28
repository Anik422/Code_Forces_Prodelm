n = int(input())
count = 0
max_value = 0
for i in range(n):
    x , y = map(int, input().split())
    count -= x
    count += y
    if count > max_value:
        max_value = count
print(max_value)