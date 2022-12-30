n = int(input())


def isIs(a):
    sum = a
    a = str(a)
    for d in a:
        sum += int(d)
    if n == sum: return int(a)
    else: return 0


check = 0
for i in range(1, n):
    if isIs(i) != 0:
        print(i)
        check = 1
        break

if check == 0: print('0')
