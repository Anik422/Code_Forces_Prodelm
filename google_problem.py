# from pprint import pprint
# sentence = "This is a common interview question"
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# pprint(char_frequency, width=1)
# char_frequency_sorted = sorted(
#     char_frequency.items(),
#      key=lambda kv: kv[1],
#      reverse=True)
# print(char_frequency_sorted)

loop = int(input())
for i in range(loop):
    Number = int(input("Please Enter any Number: "))
    list = []
    pow = 1
    while(Number > 0):
        Remainder = Number % 10
        Number = Number // 10
        list.append((Remainder)*pow)
        pow = pow * 10
    print(len(list))
    list_final = list[::-1]
    for i in range(len(list)):
        print((list_final[i]), end="  ")
