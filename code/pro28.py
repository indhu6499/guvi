a=int(input(" "))
on=list(map(int,input().split()))
on.sort()
s=0
s1=0
for i in range(len(on)):
    if on[i]>=s:
        s1=s1+1
    s=s+on[i]
print(s1)
