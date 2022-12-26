testCase = int(input())

for i in range(testCase):
    istr = input()
    info = istr.split(' ')
    for c in info[1]:
        print(c*int(info[0]), end='')
    print()
