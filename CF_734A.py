num = int(input())
str1 = input()
a = 0
b = 0
for i in range(num):
    if str1[i] == 'A':
        a += 1
    elif str1[i] == 'D': 
        b += 1

if a > b:
    print("Anton")
elif a < b:
    print("Danik")
elif a == b:
    print("Friendship")
    
    
        