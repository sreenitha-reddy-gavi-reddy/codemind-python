s=input()
s1=input()
s=s.lower()
s1=s1.lower()
s=s.split()
s1=s1.split()
for i in s1:
    for j in s:
        if i==j:
            print(i,end=' ')