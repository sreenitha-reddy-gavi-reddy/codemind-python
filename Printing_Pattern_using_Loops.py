MAX=100
def prints(a,s):
    for i in range(s):
        for j in range(s):
            print(a[i][j],end=' ')
        print()
def pattern(n):
    s=2*n-1
    f=0
    b=s-1
    a=[[0 for i in range(MAX)] for i in range(MAX)]
    while n!=0:
        for i in range(f,b+1):
            for j in range(f,b+1):
                if(i==f or i==b or j==f or j==b):
                    a[i][j]=n
        f+=1
        b-=1
        n-=1
    prints(a,s)
if __name__=='__main__':
    n=int(input())
    pattern(n)