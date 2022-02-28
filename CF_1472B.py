n = int(input())
for i in range(n):
    g1 = 0
    g2 = 0
    m = int(input())
    cand = list(map(int, input().split()[:m]))
    for j in cand:
        if j == 1:
            g1 += 1
        else:
            g2 += 1
    if (g1 % 2 == 0 and g2 % 2 == 0) or (g1 != 0 and g1 % 2 == 0 and g2 % 2 != 0):
        print("YES")
    else:
        print("NO")
