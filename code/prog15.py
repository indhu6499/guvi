b=input(" ")
y=map(int,input().split())
s=[]
for i in y:
    eat=bin(i)
    s.append(eat)
fine=sorted(s)
fine.reverse()
for j in fine:
    print(int(j,2))
