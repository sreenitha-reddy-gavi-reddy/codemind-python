a=int(input())
b=int(input())
for i in range(0,b):
    W,H=map(int,input().split())
    if W<a or H<a:
        print("UPLOAD ANOTHER")
    elif W==H:
        print("ACCEPTED")
    elif W==a and H==a:
        print("ACCEPTED")
    elif W>a or H>a:
        print("CROP IT")