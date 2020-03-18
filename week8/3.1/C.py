import math
a = int(input())
b = int(input())
for i in range(int(math.sqrt(a)),int(math.sqrt(b))):
    if i >= a : print(i*i)