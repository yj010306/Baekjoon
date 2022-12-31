n = int(input())

add = 6
pre_num = 1
ans = 1

while pre_num < 1000000000:
    if n == 1:
        print(ans)
        break
    elif pre_num + 1 <= n <= pre_num + add:
        ans += 1
        print(ans)
        break
    else:
        ans += 1
        pre_num = pre_num + add
        add += 6

