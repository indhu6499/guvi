import statistics as st
cou=int(input(" "))
array=list(map(int,input().split()))
re=False
for i in range(1,cou):
  I1=array[:i]
	I2=array[i:]
if st.mean(I1)==st.mean(I2):
  re=True
if re==True:
	 print("yes")
else:
   print("no")
