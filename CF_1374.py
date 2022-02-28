n = int(input())
for i in range(n):
    x, y, z = map(int, input().split())
    print(z-(z-y) % x)
