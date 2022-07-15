s=input().lower()
s1=input().lower()
l=[]
for i in s:
    if i not in s1:
        l.append(i)
for j in s1:
    if j not in s:
        l.append(j)
for k in sorted(set(l)):
    if k!=' ':
        print(k,end='')