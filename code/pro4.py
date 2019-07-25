a,b=map(str,input(" ").split(" "))
t=0
if len(a)>len(b):
  a,b=b,a
m=0
while m<len(a):
  t+=(ord(b[m])-ord(a[m]))
  m+=1
for r in range(r,len(b)):
  t+=ord(b[m])-ord('a')+1
print(t)
