from posixpath import split


x, y = map(int, input().split())
number_list = list(map(int,input().strip().split()))[:x]
count = 0
for z in number_list:
    if y <= z:
        if z % y == 0:
            count += (z // y)
        else:
            count += 2
    else:
        count += 1
print(count)