from itertools import permutations
p, o = map(int, input(" ").split(" "))
y = list(map(int, input().split()))
for i in permutations(y, 2):
    if sum(i) == o:
        print('yes')
        break
else:
    print('no')
