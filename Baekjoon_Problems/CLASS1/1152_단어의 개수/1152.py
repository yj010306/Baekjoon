initStr = str(input())

infoList = initStr.split(' ')

if infoList[len(infoList)-1] == '' and infoList[0] != '':
    print(len(infoList)-1)
elif infoList[len(infoList)-1] != '' and infoList[0] == '':
    print(len(infoList)-1)
elif infoList[len(infoList)-1] == '' and infoList[0] == '':
    print(len(infoList)-2)
else:
    print(len(infoList))
