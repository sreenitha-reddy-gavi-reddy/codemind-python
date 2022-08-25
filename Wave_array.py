n=int(input())
a=list(map(int,input().split()))
c=0
if a[0]<a[1]:
    if a[n-2]<a[n-1] and a[n-1]>a[0]:
        c=1
    else:
        c=0
    for i in range(1,n-1,2):
        if a[i-1]<a[i] and a[i]>a[i+1]:
            c=1
        else:
            c=0
            break
elif a[0]>a[1]:
    if a[n-2]>a[n-1] and a[n-1]<a[0]:
        c=1
    else:
        c=0
    for i in range(1,n-1,2):
        if a[i-1]>a[i] and a[i]<a[i+1]:
            c=1
        else:
            c=0
            break
if c==0:
    print("no")
else:
    print("yes")