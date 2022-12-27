```python
str = str(input())
info = str.split(' ')

val = 0
for i in info:
    val += int(i)*int(i)

print(val%10)
```
