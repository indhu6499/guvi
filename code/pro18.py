n,m=map(int,input(" ").split(" "))
t=[]
x=0
for a in range(n):
    t.append(list(map(int,input().split())))   
for a in range(n):
    for j in range(m-1):
        for k in range(j+1,m+1):
            if t[a][j:k]==[1]*len(t[a][j:k]):
                 if all(t[p+a][j:k]==[1]*len(t[p+a][j:k]) for p in range(len(t[a][j:k])-1)):
                     if len(t[a][j:k])>x:
                        x=len(t[a][j:k])
if len(t)==1 and len(t[0])==1 and t[0][0]==1:
    print(1)
for a in range(x):
    print(*[1]*x)
