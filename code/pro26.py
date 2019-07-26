n=int(input(" "))
s=list(map(int,input().split()))
a=[]
num=1
for i in s:
  if i not in a:
    a.append(i)
for i in range(0,len(a)-1):
  if a[i]<a[i+1]:
    num+=1
print(num)
