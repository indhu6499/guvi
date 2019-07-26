b,c=map(int,input(" ").split(" "))
array=list(map(int,input().split()))
array.sort(reverse=True)
s=0
to=c
for i in array:
    if to>=i:
        rem=int(to/i)
        s+=rem
        to=to - (i*rem)
    if to==0:
        break
if to==0:
    print(s)
else:
    print("it's not possible to sum up coins in such a way that they um upto",c)
