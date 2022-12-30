t = int(input())


def room(h, n):
    return n%h*100 + (n//h+1)


for i in range(t):
    info = str(input()).split(' ')
    for j in range(3):
        info[j] = int(info[j])
    if room(info[0], info[2]) < 101: print(info[0]*100 + room(info[0], info[2])-1)
    else: print(room(info[0], info[2]))
