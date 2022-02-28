t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()[:n]))
    sl = len(s)
    result = 0
    bool = True
    for j in range(sl):
        for k in range(j+1, sl):
            p = abs(s[j] - s[k])
            if bool == True:
                result = p
                bool = False
            elif p < result:
                result = p
    print(result)
