x=int(input())
s=0
for i in range(x):
    n=input()
    l=len(n)
    for j in n:
        if j>='0' and j<='9':
            s+=1
    if l==s:
        print('True')
    else:
        print('False')
    s=0