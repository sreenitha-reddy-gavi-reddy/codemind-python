a=int(input())
b=int(input())
c=0
m=0
for i in range(1,a):
    if a%i==0:
        c+=i
for j in range(1,b):
    if b%j==0:
        m+=j
if c==b and m==a:
    print("Amicable")
else:
    print("Not Amicable")