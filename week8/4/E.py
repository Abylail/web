n = int(input())
a = input().split()
for i in range (n):
    a[i]=int(a[i])

for i in range(n-1):
    if a[i]*a[i+1]>0:
        print('YES')
        exit(0)
print('NO')