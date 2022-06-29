n=int(input())
m=0
for i in range(1,n+1,1):
    for j in range(1,n-1,1):
        print(j,end="")
        if j==n-2:
            m=j
            for k in range(m-1,0,-1):
                print(k,end="")
    print()