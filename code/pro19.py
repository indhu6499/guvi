c1=int(input(" "))
ar=[]
s1=[]
for i in range(c1):
    ar.append(list(map(int,input().split())))
for llist in ar:
    for num in llist:
        s1.append(num)
s1.sort()
for i in s1:
    print(i,end=' ')
