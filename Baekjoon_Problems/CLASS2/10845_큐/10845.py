import sys

List = []

n = int(input())

for i in range(n):
    fTmp = sys.stdin.readline()
    tmp = fTmp.strip().split(' ')
    if tmp[0] == 'push':
        List.append(int(tmp[1]))
    elif tmp[0] == 'pop':
        if len(List) == 0:
            print('-1')
        else:
            print(List[0])
            del List[0]
    elif tmp[0] == 'size':
        print(len(List))
    elif tmp[0] == 'empty':
        if len(List) == 0: print('1')
        else: print('0')
    elif tmp[0] == 'front':
        if len(List) == 0:
            print('-1')
        else:
            print(List[0])
    elif tmp[0] == 'back':
        if len(List) == 0:
            print('-1')
        else:
            print(List[len(List)-1])
