lenList = [1 for i in range(3)]

def ss(li):
    ans = 0
    for i in range(3):
        if li.index(max(li)) != i:
            ans += li[i]**2
    return ans

while True:
    lenList = str(input()).split(' ')
    lenList[0] = int(lenList[0])
    lenList[1] = int(lenList[1])
    lenList[2] = int(lenList[2])
    if lenList[0] == 0:
        break
    else:
        if max(lenList)**2 == ss(lenList):
            print('right')
        else: print('wrong')
