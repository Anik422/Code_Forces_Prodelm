
str1 = input()
upper = 0
lower = 0
for i in range(len(str1)):
    if str1[i].islower():
        lower += 1
    elif str1[i].isupper():
        upper += 1

if upper <= lower:
    print(str1.lower())
elif upper > lower:
    print(str1.upper())
    