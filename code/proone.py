I=int(input(" "))
N=[]
for X in range(0,I):
   N.append(input())
I1=len(K[0])
P=""
for X in range(0,I1):
   C=N[0][X]
   F=0
   for Y in range(0,I):
        if(C!=N[Y][X]):
           F=1
   if(F==0):
     P=P+C
   else:
     break
print(P)
