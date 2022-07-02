n=input()
a=list(n)
b=set(n)
if len(a)==len(b):
    print("Unique Number")
else:
    print("Not Unique Number")