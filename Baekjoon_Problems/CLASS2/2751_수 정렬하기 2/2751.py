import sys

n = int(input())
numList = []

for i in range(n):
    numList.append(int(sys.stdin.readline()))

numList.sort()

for i in range(n):
    print(numList[i])
