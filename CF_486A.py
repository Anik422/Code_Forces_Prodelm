import math
n = int(input())
if n % 2 == 0:
    result = int(n/2)
else:
    result = int(math.ceil(n/2)* -1)
print(result)