stairs = list(map(int, input().split()))
route = [0]*len(stairs)
way = [True, False]

route[0], route[1] = stairs[0], stairs[1]
for i in range(2, len(route)):
    minimum = min(route[i-1], route[i-2])
    way.append(minimum == route[i-1])
    route[i] = minimum+stairs[i]
print(route[-1])


finway = []
while way:
    if way[-1]:
        finway[:0] = ['одна ступенька\n']
        way = way[:-1]
    else:
        finway[:0] = ['две ступеньки\n']
        way = way[:-2]
print(*finway, sep = '')