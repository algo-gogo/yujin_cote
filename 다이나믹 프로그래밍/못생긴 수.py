'''
못생긴 수란 오직 2, 3, 5만을 소인수로 가지는 수를 의미한다.
다시 말해 오직 2, 3, 5를 약수로 가지는 합성수를 의미한다.
1은 못생긴 수라고 가정한다.
따라서 못생긴 수들은 {1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15 ...} 순으로 이어지게 된다.
이때, n번째 못생긴 수를 찾는 프로그램을 작성하세요.
1 <= n <= 1,000
'''

n = int(input())

d = [1]


for i in range(n+1):
    d.append(d[i]*2)
    d.append(d[i]*3)
    d.append(d[i]*5)

result = set(d)

print(result)

print(list(result)[n-1])
