def split(word):
    return list(word)
user_input = input()
user_input2 = input()

a = split(user_input)
b = split(user_input2)
b.reverse()
for i in range(len(a)):
    if a[i] == b[i]:
        continue
    else:
        print("NO")
        break
else:
    print("YES")
