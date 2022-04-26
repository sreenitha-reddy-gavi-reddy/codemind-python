n=int(input())
import math
root=math.sqrt(n)
if int(root+0.5)**2==n:
    print('True')
else:
    print('False')