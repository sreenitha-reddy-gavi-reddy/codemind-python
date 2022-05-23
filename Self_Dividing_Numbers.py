a=int(input())
b=int(input())
l=0
for i in range(a,b+1):
    x=len(str(i))
    c=i
    while c!=0:
        j=c%10
        if j!=0 and i%j==0:
            l+=1
        c=c//10
    if l==x:
        print(i,end=' ')
    l=0