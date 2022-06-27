n=int(input())
c=0
c1=0
a=list(map(int,input().split()))
for i in range(n):
    if a[i]%2==0:
        c+=1
    else:
        c1+=1
print(c,c1,end=' ')