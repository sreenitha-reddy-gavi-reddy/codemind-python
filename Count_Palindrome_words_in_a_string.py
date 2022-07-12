def pal(s):
    if s.lower()==s.lower()[::-1]:
        return True
def countpal(str):
    count=0
    l=str.split(" ")
    for i in l:
        if(pal(i)):
            count+=1
    print(count)
s=input()
countpal(s)