from tokenize import Number


n = int(input())
count = 0
for i in range(n):
    m = int(input())
    number = list(map(int, input().split()[:m]))
    for j in range(m):
        if j % 2 == 0:
            count -= number[j] 
        else:
            count += number[j] 
    abs_count = abs(count)
    if len(number) == 1:
        print('YES')
    elif abs_count == 1 or abs_count == 0:
        print('Yes')
    elif abs_count > 1 :
        print('NO')