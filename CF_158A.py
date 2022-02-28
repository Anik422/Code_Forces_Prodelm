x, y = [int(x) for x in input().split()]
count = 0
number_list = list(map(int, input().split()))
for item in number_list:
    if item >= number_list[y-1] and item > 0:
        count += 1
    else:
        break
print(count)
    