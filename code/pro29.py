n=int(input(" "))

a=0

x=0

b=[]

while a<90 and a<n:

  s=0

  for j in str(n-a):

    s+=int(j)

  if s+(n-a)==n:

    x+=1

    b.append(n-a)

  a+=1

print(x)

for a in b:

  print(a)
 
