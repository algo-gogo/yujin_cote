'''
N개의 수로 이루어진 수열
수와 수 사이에 끼울 수 있는 N-1개의 연산자
연산자는 + - * / 네개 사칙연산쓰~
수와 수 사이에 연산자를 하나씩 넣어서 수식을 하나 만들 수 있다.
수의 순서는 바꾸면 안 된다.
N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것.
'''
'''
1+2*3
전위계산법으로생각해야할듯
+1*23이 된다
숫자 하나씩 스택에서 뽑아서 다시 스택에 쌓고 연산자 만나면 숫자두개뽑음

연산자 우선순위 상관없어서 문제인가???????
'''

from itertools import permutations

N = int(input())

numbers = list(map(int,input().split()))

operators = ["+", "-", "*", "/"]

operator_counts = list(map(int,input().split()))


def calc(expression, stack):
    if len(expression) == 0:
        return stack[0]
    
    temp = expression.pop()

    if temp not in operators:
        stack.append(temp)
    else:
        if temp == "+":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)
        elif temp == "-":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 - num2)
        elif temp == "*":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 * num2)
        elif temp == "/":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 / num2)
    return calc(expression, stack)

def make_expression(numbers, operator_counts):
    operater_list = []
    for i in range(4):
        for j in range(operator_counts[i]):
            operater_list.append(operators[i])

    candidates = permutations(operater_list, len(operater_list))

    min_value = None
    max_value = None

    for i in candidates:
        expression = numbers[:]
        for j in range(len(i)):
            expression.insert(j*2, i[j])
        temp = calc(expression, [])

        print( expression, temp )

        if min_value == None and max_value == None:
            min_value = max_value = temp
        else:
            min_value = min(temp, min_value)
            max_value = max(temp, max_value)

    print( max_value )
    print( min_value )


make_expression(numbers, operator_counts)

    
