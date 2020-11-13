# Transform the Expression
t = int(input())
expression = []

for i in range(t):
    expression.append(input().strip())
print(expression)

res = ''
stack = []

for express in expression:
    for char in express:
        if char.isalpha():
            res += char
        elif char == ')':
            res += stack[-1]
            stack.pop()
        elif char != '(':
            stack.append(char)

print(res)
