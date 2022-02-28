s = input()
str_len = len(s)
set_list = set()
for i in range(1, str_len-1, 3):
    set_list.add(s[i])
print(len(set_list))

# print(s[1])
# print(s[4])