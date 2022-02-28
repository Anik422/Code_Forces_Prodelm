n = int(input())
for i in range(1, n+1):
    x = int(input())
    r = []
    c = 1
    while (x > 0):
        k = x % 10
        x = x // 10
        r.append(k*c)
        c *= 10
    count = 0
    d = r[::-1]
    for k in d:
        if k > 0:
            count += 1
    print(count)
    for l in d:
        if l > 0:
            print(l, end=" ")
    print()
