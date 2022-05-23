a,b=map(int,input().split())
for i in range(1,b+1):
    c=a*i
    if i%2!=0:
        print(a,'x',i,'=',c)