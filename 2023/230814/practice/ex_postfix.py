'''
(6+5*(2-8)/2)
6528-*2/+
'''

# 후위 표기법으로 만들기

stack = [0] * 100
top = -1
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

fx = '(3+4+5+6+7)'
susik = ''
for x in fx:
    if x not in '(+-*/)':
        susik += x
    elif x == ')':
        while stack[top] != '(':    # peek
            susik += stack[top]
            top -= 1
        top -= 1    # '(' 버림. pop

    else:    # in '(+=*/'
        if top == -1 or isp[stack[top]] < icp[x]:    # 토큰의 우선순위가 더 높으면
            top += 1    # push
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top += 1
            stack[top] = x

print(susik)

# 후위 표기식 계산하기

stack = [0] * 100
top = -1
s = susik
for x in s:
    if x not in '+-/*':    # 피연산자면...
        top += 1    # push(x)
        stack[top] = int(x)
    else:
        op1 = stack[top]  # pop()
        top -= 1
        op2 = stack[top]  # pop()
        top -= 1
        if x == '+':    # op2 + op1
            top += 1    # push()
            stack[top] = op2 + op1
        elif x == '-':
            top += 1
            stack[top] = op2 - op1
        elif x == '/':
            top += 1
            stack[top] = op2 / op1
        elif x == '*':
            top += 1
            stack[top] = op2 * op1

print(stack[top])