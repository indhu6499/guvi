cot=int(input(" "))
array=list(map(int,input().split()))
array.sort(reverse=True)

s=0
s1=0
result=[]
for i in range(0,cot,2):
    s=s+array[i]
for j in range(1,cot,2):
    s1=s1+array[j]
result.append([s,s1])

for i in result:
    print(i[0] if i[0]>i[1] else i[1])
