n = int(input())

infoList = []

for i in range(n):
    tmp = str(input()).split(' ')
    infoList.append([int(tmp[0]), int(tmp[1])])

ans = sorted(infoList, key= lambda x: (x[0], x[1]))

for i in range(n):
    print(ans[i][0], ans[i][1])
