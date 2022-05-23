def hcf(a,b):
    a>b
    a,b=b,a
    c=a
    while True:
        if a%c==0 and b%c==0:
            return c
        c-=1
a,b=map(int,input().split())
print(hcf(a,b))