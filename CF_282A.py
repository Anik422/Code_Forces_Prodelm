n = int(input())
x = 0
for i in range(n):
    x_str = input()
    if x_str == "X++":
        x = x + 1
    elif x_str == "++X":
        x = 1 + x
    elif x_str == "--X":
        x = -1 + x
    elif x_str == "X--":
        x = x - 1
print(x)
