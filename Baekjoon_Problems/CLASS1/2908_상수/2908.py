inputStr = str(input())
info = inputStr.split(' ')

num1 = int(info[0])
num2 = int(info[1])


def reverse(a):
    return a%10*100 + a//10%10*10 + a//100


num1 = reverse(num1)
num2 = reverse(num2)

print(max(num1, num2))
