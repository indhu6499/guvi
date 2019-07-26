cout=int(input(" "))
array=list(map(int,input().split()))
array.sort(rev=True)

A=0
A1=0
res=[]
for i in range(0,cout,2):
    sum=sum+array[i]
for j in range(1,cout,2):
    A1=A1+array[j]
res.append([A,A1])

for i in res:
    print(i[0] if i[0]>i[1] else i[1])
