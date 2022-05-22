a=int(input())
c=a
rev=0
while c!=0:
    h=c%10
    rev=rev*10+h
    c=c//10
if a==rev:
    print("True")
else:
    print("False")