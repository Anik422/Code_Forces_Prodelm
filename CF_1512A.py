n = int(input())
for i in range(n):
    x = int(input())
    num = list(map(int, input().split()[:x]))
    num2 = sorted(num)
    if num2[0] != num2[1]:
        print(num.index(num2[0])+1)
    elif num2[-1] != num2[-2]:
        print(num.index(num2[-1])+1)
