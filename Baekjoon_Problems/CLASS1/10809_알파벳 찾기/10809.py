al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q','r','s','t','u','v','w','x','y','z']

s = str(input())


def isIn(c):
    for a in s:
        if c == a:
            return s.index(c)
    return -1


for i in al:
    print(isIn(i), end=' ')
