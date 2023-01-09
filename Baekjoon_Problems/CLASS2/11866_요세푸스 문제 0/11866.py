tmp = str(input()).split(' ')

n = int(tmp[0])
k = int(tmp[1])

info = [i+1 for i in range(n)]
ans = []

cnt = 0
infoIndex = 0
while len(ans) != n:
    while cnt != k:
        if info[infoIndex%n] != 0:
            cnt += 1
            infoIndex += 1
        else:
            infoIndex += 1
    ans.append(info[(infoIndex-1)%n])
    info[(infoIndex - 1) % n] = 0
    cnt = 0

for i in range(n):
    if n == 1:
        print(f'<{ans[i]}>')
    elif i == 0:
        print(f'<{ans[i]}, ', end='')
    elif i == n-1:
        print(f'{ans[i]}>')
    else:
        print(f'{ans[i]}, ', end='')

