inputNum = str(input()).split(' ')
inputNum[0] = int(inputNum[0])
inputNum[1] = int(inputNum[1])

ansMin = 0
for i in range(1,max(inputNum[0], inputNum[1])+1):
    if inputNum[0]%i == 0 and inputNum[1]%i == 0:
        ansMin = i

com1 = inputNum[0]
com2 = inputNum[1]

while com1 != com2:
    if com1 > com2:
        com2 += inputNum[1]
    elif com1 < com2:
        com1 += inputNum[0]

print(ansMin)
print(com1)
