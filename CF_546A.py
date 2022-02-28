k, n, w = map(int, input().split())
m = (w * (w+1) * k )// 2
if m <= n:
    print("0")
else:
    print(m-n)