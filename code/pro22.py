cout=int(input(" "))
arr=list(map(int,input().split()))
arr.sort(rev=True)

A=0
A1=0
res=[]
for i in range(0,cout,2):
    sum=sum+arr[i]
for j in range(1,cout,2):
    A1=A1+arr[j]
res.append([A,A1])

for i in res:
    print(i[0] if i[0]>i[1] else i[1])
