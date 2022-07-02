N=int(input())
people=[]
house=[]
for i in range(N):
    people.append(int(input()))
for i in range(N):
    house.append(int(input()))
count=0
for i in range(N):
    if people[i]>house[N-1]:
        count+=1
print(count)