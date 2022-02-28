num = int(input())
for item in range(num):
    User_str = input()
    str_len = len(User_str)
    if str_len > 10:
        a = str(User_str[0])
        b = str(len(User_str)-2)
        c = str(User_str[-1])
        print(a+b+c)
    else:
        print(User_str)
    
