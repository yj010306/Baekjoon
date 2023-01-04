def isSo(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0: cnt+=1
    if cnt == 2: return True
    else: return False


N = int(input())

info = str(input()).split(' ')

ans = 0
for i in range(N):
    if isSo(int(info[i])): ans += 1

print(ans)
