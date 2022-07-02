n=input().strip()
p=n[-2:].lower()=='pm'
t=list(map(int,n[:-2].split(':')))
if p and t[0]<12:
    t[0]+=12
if not p and t[0]==12:
    t[0]=0
print(':'.join(map(lambda x:str(x).rjust(2,'0'),t)))