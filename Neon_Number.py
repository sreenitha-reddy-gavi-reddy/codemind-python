n=int(input())
s=0
r=n*n
for i in range(r):
    i=r%10
    s=s+i
    r=r//10
sum=int(s)
if n==sum:
    print("Neon Number")
else:
    print("Not Neon Number")