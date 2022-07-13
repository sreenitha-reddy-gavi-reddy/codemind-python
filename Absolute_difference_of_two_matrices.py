n=int(input())
l=[]
m=[]
for i in range(2):
    for j in range(n):
        a=list(map(int,input().split()))
        if i==0:
            for k in a:
                l.append(k)
        if i==1:
            for h in a:
                m.append(h)
for u in range(n*n):
    if u%n==(n-1):
        print(abs(m[u]-l[u]))
    else:
        print(abs(m[u]-l[u]),end=' ')