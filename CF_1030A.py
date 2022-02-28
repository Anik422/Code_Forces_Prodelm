n = int(input())
number_list = list(map(int, input().strip().split()))[:n]
for item in number_list:
    if 0 < item:
        print("HARD")
        break
    else:
        pass
else:
    print("EASY")