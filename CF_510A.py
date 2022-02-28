if __name__ == '__main__':
    result = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        result.append([name, score])
    print(result[1])
# a, b = map(int, input().split())
# c = True
# for i in range(1,a+1):
#     if i % 2 == 0:
#         if c == True:
#             print(f"{'.'*(b-1)}#")
#             c = False
#         elif c == False:
#             print(f"#{'.'*(b-1)}")
#             c = True
#     else:
#         print('#'*b)
