'''
정수 X가 주어질 때 정수 X에 사용할 수 있는 연산
1. X가 5로 나누어 떨어지면 5로 나눔
2. X가 3으로 나누어 떨어지면 3으로 나눔
3, X가 2로 나누어 떨어지면 2로 나눔
4. X에서 1을 뺌

이것부터 뭔문제인지모르겠다만..

10 -> 5로 나눔 2->2로나눔 총 2.
'''

X = int(input())

d = [0] * 1000001

# calc_count = 0

for i in range( 2, X+1 ):
    if i % 5 == 0:
        d[i] = d[i//5] + 1
    elif i % 3 == 0:
        d[i] = d[i//3] + 1
    elif i % 2 == 0:
        d[i] = d[i//2] + 1
    else:
        d[i] = d[i-1] + 1

    print( i, d[i] )

print( d[0:20] )