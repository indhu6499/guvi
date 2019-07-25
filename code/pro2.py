from itertools import combinations
v,a=map(int,input(" ").split(" "))
I1=len(str(v))
I2=list(combinations(str(v),l1-u))
I2=sorted(I2)
print(*I2[0],sep='')
