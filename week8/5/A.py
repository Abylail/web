def min(a):
    m = int(100000)
    for i in range (len(a)-1):
        if a[i]<m:
            m = a[i]
    return m;

a = input().split()
for i in range (len(a)):
    a[i]=int(a[i])
print(min(a))