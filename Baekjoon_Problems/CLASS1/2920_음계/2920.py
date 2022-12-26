str = str(input())

info = str.split()


def isAscending():
    ans = 1
    for i in range(8):
        if int(info[i]) != i+1:
            ans = 0
            return ans
    return ans


def isDescending():
    ans = 1
    for i in range(8):
        if int(info[i]) != 8-i:
            ans = 0
            return ans
    return ans


if int(info[0]) == 1:
    if isAscending() == 1: print('ascending')
    else: print('mixed')

elif int(info[0]) == 8:
    if isDescending() == 1:
        print('descending')
    else:
        print('mixed')

else: print('mixed')
