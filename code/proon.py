A1=int(input(" "))
I=[]
for X in range(0,A1):
   I.append(input())
A2=len(I[0])
J=""
for X in range(0,A2):
   C=I[0][X]
   F=0
   for Y in range(0,A1):
        if(C!=I[Y][X]):
           F=1
   if(F==0):
     J=J+C
   else:
     break
print(J)
