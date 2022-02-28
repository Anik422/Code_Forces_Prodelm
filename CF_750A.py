a, b = map(int, input().split())
p = 240 - b
coun = 0
gononakari = 0
for i in range(1, a+1):
    coun += 5 * i
    if coun <= p:
        gononakari += 1
    else:
        break
print(gononakari)

    
