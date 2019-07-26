si=int(input(" "))
a1=2**si
list=[]
for i in range(0,a1):
    I=bin(i)[2:].zfill(si)
    if(len(I)<len(bin(2**si-1)[2:])):
        list.append([I.count("1"),I])
    else:
        list.append([I.count("1"),I])
list.sort()
for i in range(len(list)):
    print(list[i][1])
