def is_prime(a):
    i=2
    v=0
    while i!=a:
        if a%i==0:
            v=1
        i+=1
    if v==0:
        return a
x=int(input())
for i in range(x):
    y=int(input())
    b=y
    for j in range(y,2-1,-1):
        if is_prime(j):
            n=j
            break
    while b!=0:
        if is_prime(b):
            m=b
            break
        b+=1
    if(y-n)<(m-y):
        print(n)
    elif(y-n)==(m-y):
        print(n)
    else:
        print(m)