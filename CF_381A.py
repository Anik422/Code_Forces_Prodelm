n = int(input())
number = list(map(int, input().split()[:n]))
sereja = 0
dima = 0
for i in range(n):
    if i % 2 != 0:
        dima += number[i]
    elif i % 2 == 0:
        sereja += number[i]
if sereja > dima:
    print(f"{sereja} {dima}")
else:
    print(f"{dima} {sereja}")
