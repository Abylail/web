n = int(input())
a = input().split()
j = int(0)
for i in range (n-1):
    a[i]=int(a[i])
    if a[i]< int(a[i+1]):
        j=j+1

print(j)