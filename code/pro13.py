wod = (input(" "))
if wod> 1:
    for i in range(2, wod):
        if (wod% i) == 0:
            print(wod, "no")
            break
    else:
        print(wod,"yes")
else:
    print(wod, "no")
