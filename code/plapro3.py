x=input(" ")
n=0
while(x>0):
    dig=x%10
    n=n*10+dig
    x=x//10
print(n)
