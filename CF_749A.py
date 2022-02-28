n = int(input())
count = 0
list = []
while n != 0:
    if n != 3:
        n -= 2
        list.append(2)
        count += 1
    else:
        n -= 3
        list.append(3)
        count += 1
print(count)
for i in list:
    print(i, end=' ')
