from string import ascii_letters

alLi = list(ascii_letters)

alCnt = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
         'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
         'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
         'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

inputStr = str(input())

for i in inputStr:
    for c in alLi:
        if c == i:
            if alLi.index(c) < 26:
                alCnt[c.upper()] += 1
            else:
                alCnt[c] += 1

maxCnt = 0
ans = 0
same = 0
for i in alLi[26:]:
    if alCnt[i] > maxCnt:
        maxCnt = alCnt[i]
        ans = i
        same = 1
    elif alCnt[i] == maxCnt:
        same += 1

if same > 1:
    print('?')
else:
    print(ans)
