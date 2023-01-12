import sys

List = []

n = int(input())

for i in range(n):
    fTmp = sys.stdin.readline()
    tmp = fTmp.strip().split(' ')
    if tmp[0] == 'push_front':
        List.insert(0, tmp[1])
    elif tmp[0] == 'push_back':
        List.append(tmp[1])
    elif tmp[0] == 'pop_front':
        if len(List) == 0: print('-1')
        else:
            print(List[0])
            del List[0]
    elif tmp[0] == 'pop_back':
        if len(List) == 0: print('-1')
        else:
            print(List[len(List)-1])
            List.pop()
    elif tmp[0] == 'size':
        print(len(List))
    elif tmp[0] == 'empty':
        if len(List) == 0: print('1')
        else: print('0')
    elif tmp[0] == 'front':
        if len(List) == 0: print('-1')
        else:
            print(List[0])
    elif tmp[0] == 'back':
        if len(List) == 0: print('-1')
        else:
            print(List[len(List)-1])
