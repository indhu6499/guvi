n1,n2=input(" ").split(" ")
cost=abs(len(n1)-len(n2))
for i in range(len(n1)):
    if len(n2)==1 and n2[i] in n1:
        break
    if n1[i] != n2[i]:
        cost+=1 
print(cost)
