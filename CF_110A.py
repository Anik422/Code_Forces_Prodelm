from unicodedata import numeric


num = input()
for item in range(len(num)):
    if num[item] != '4' or num[item] != '7':
        print("no")
