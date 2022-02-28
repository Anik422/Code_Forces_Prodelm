n = int(input())
for i in range(n):
    result = ""
    x_str = input()
    result += x_str[0]
    for j in range(1, len(x_str)-1, 2):
        result += x_str[j]
    result += x_str[-1]
    print(result)
#     for j in range(len(x_str)-1):
#         if x_str[j] != result[-1]:
#             result = result + x_str[j]
#         else:
#             pass
#     if x_str[-1] != result[-1]:
#         result = result + x_str[-1]
#     print(result[1:])
