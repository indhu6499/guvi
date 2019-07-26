num=input(" ")
s=0
for i in range(0,len(num)):
    s1=num[0:i]+num[i+1::]
    if int(s1)%8==0:
        s=1
        break
if s==1:
    print("yes")
else:
    print("no")
