def li(arr,size):
    resu=[]
    cot=1
    for i in range(0,size-1):
        if arr[i]<arr[i+1]:
            cot+=1
        else:
            resu.append(cot)
            cot=1
    resu.append(cot)
    print(max(resu))
s=int(input())
arr=list(map(int,input(" ").split(" ")))
li(arr,s)
