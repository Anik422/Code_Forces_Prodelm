n = int(input())
bills = [100, 20, 10, 5, 1]
result = 0
for i in bills:
    m = n//i
    n = n - (i * m)
    result += m
print(result)