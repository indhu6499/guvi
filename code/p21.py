import statistics as st
c=int(input(" "))
ar=list(map(int,input().split()))
r=False
for i in range(1,c):
    A1=ar[:i]
    A2=ar[i:]
    if st.mean(A1)==st.mean(A2):
        r=True
if r==True:
    print("yes")
else:
    print("no")
