p,o = [int(i) for i in input(" ").split(" ")]
m = []
List = [int(i) for i in input().split()]
for _ in range(o):
    l, k = [int(i) for i in input().split()]
    m.append(min(List[l-1:k]))
for i in m:
    print(i)
