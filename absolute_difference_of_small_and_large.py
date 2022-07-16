s=input()
x=s.split(" ")
for i in x:
    m=ord(min(i))
    ma=ord(max(i))
    print(abs(m-ma),end=' ')