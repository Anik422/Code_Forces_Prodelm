
from cgitb import reset
from typing import Tuple


hostName1 = input()
hostName2 = input()
allNameLetters = list(input())
addHostName = list(hostName1 + hostName2)
result = False
for i in allNameLetters:
    if i not in  addHostName:
        print("NO")
        result = True
        break
if result == False:
    print("YES")




# if result == 0:
#     print('YES')
# else:
#     print('NO')


