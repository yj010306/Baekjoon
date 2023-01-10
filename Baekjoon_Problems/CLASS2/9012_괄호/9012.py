stack = []

n = int(input())
for i in range(n):
    tmp = str(input())
    for c in tmp:
        if c == '(':
            stack.append('(')
        elif len(stack) != 0 and c == ')':
            stack.pop()
        else:
            stack.append(')')
            break

    if len(stack) == 0: print('YES')
    else: print('NO')

    stack.clear()
