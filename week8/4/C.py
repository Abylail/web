n = int(input())
a = input().split()
j = int(0)
for i in range (n):
    a[i]=int(a[i])
    if a[i]>0:
        j=1+j
print(j)