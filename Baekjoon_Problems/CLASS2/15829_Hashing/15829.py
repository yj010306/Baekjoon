from string import ascii_lowercase

alLi = list(ascii_lowercase)

n = int(input())
inputStr = str(input())

cnt = 0
ans = 0
for i in inputStr:
    ans += (alLi.index(i)+1) * (31**cnt)
    cnt += 1

print(ans % 1234567891)
