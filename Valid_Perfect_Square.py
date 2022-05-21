import math
a=int(input())
while a:
    x=int(input())
    r=math.sqrt(x)
    if int(r+0.5)**2==x:
        print("True")
    else:
        print("False")
    a-=1