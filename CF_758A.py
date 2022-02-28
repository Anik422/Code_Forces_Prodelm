n = int(input())
number_list = sorted(list(map(int, input().split()[:n])))
count = 0
for i in range(len(number_list)-1):
    count += (number_list[-1]-number_list[i])
print(count)
