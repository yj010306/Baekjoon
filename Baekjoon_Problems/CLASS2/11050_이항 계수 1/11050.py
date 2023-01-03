info = str(input()).split(' ')
info[0] = int(info[0])
info[1] = int(info[1])

a = 1
b = 1
if info[1] == 0: print(a)

elif info[0]//2 >= info[1]:
    for i in range(info[1]):
        a *= info[0]
        info[0] -= 1

    for i in range(1, info[1]+1):
        b *= i

    print(int(a/b))

elif info[0]//2 < info[1]:
    info[1] = info[0] - info[1]

    for i in range(info[1]):
        a *= info[0]
        info[0] -= 1

    for i in range(1, info[1] + 1):
        b *= i

    print(int(a / b))
