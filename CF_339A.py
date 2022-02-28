str1 = input().split("+")
sort_list = sorted(str1)
for item in range(0, len(sort_list)):
    if item == len(sort_list)-1:
        print(f"{sort_list[item]}",end ='')
    else:
        print(f"{sort_list[item]}+",end ='')
