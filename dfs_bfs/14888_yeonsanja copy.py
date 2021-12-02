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
전위계산법으로생각해야할듯 => 후위계산법으로일단했는데 뭐지이거 이상한듯..
+1*23이 된다
숫자 하나씩 스택에서 뽑아서 다시 스택에 쌓고 연산자 만나면 숫자두개뽑음

뭐지??????모르겠음??>...


백준은
재귀
깊이가
1000이래
...
...


'''

from itertools import permutations

N = int(input())

numbers = list(map(int,input().split()))

operators = ["+", "-", "*", "/"]

operator_counts = list(map(int,input().split()))


def calc(expression, value, index):
    if len(expression) == index:
        return value
    
    temp = expression[index]

    if temp not in operators:
        value = temp
    else:
        index += 1
        num = expression[index]
        if temp == "+":
            value += num
        elif temp == "-":
            value -= num
        elif temp == "*":
            value *= num
        else:
            if(num != 0):
                value = int(value / num)
            else:
                value = 0
    return calc(expression, value, index+1)

def make_expression(operator_counts):
    operater_list = []
    for i in range(4):
        for j in range(operator_counts[i]):
            operater_list.append(operators[i])

    return set(permutations(operater_list, len(operater_list)))

min_value = 1000000000
max_value = -1000000000

'''def prunning(candidates, min_value, max_value):
    if( len(candidates) == 0 ):
        print( max_value )
        print( min_value )
        return

    op = candidates[0]
    expression = numbers[:]
    for i in range(N-1):
        expression.insert(i*2+1, op[i])

    temp = calc(expression,0,0)

    candidates.remove(op)

    return prunning(candidates, min(temp, min_value), max(temp, max_value))
'''

def prunning(candidates, min_value, max_value):
    for op in candidates:
        expression = numbers[:]
        for i in range(N-1):
            expression.insert(i*2+1, op[i])

        temp = calc(expression,0,0)

        min_value = min(temp, min_value)
        max_value = max(temp, max_value)

    print( max_value )
    print( min_value )


prunning(make_expression(operator_counts), min_value, max_value)

    
