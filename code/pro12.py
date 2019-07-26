m,n=map(int,input(" ").split(" "))
po=list(map(int,input().split()))
I1=[]
for i in range(0,n):
     a,b=map(int,input().split())
     I1.append([a,b])
for i in range(n):
     lower=I1[i][0]
     upper=I1[i][1]
     s=sum(po[lower-1:upper])
     print(s)
