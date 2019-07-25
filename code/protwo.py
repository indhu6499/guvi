from itertools import combinations
p,u=map(int,input(" ").split(" "))
A1=len(str(p))
A2=list(combinations(str(p),l1-u))
A2=sorted(A2)
print(*A2[0],sep='')
