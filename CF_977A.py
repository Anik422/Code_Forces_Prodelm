user_inpute , counter = [int(x) for x in input().split()]
for item in range(counter):
    if user_inpute % 10 == 0:
        user_inpute = user_inpute / 10
    else:
        user_inpute -= 1
print(int(user_inpute))
