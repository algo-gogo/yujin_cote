'''
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
크기가 5인 정수 삼각형 모습.
맨위층부터 하나를 선택해서 아래층으로 내려올 때,
이때까지 선택된 수의 합이 최대가 되는 경로
삼각형 크기는 1이상 500이하. 각 수는 최대 9999임.
'''

n = int(input())

triangle = []

for i in range(n):
    triangle.append(list(map(int,input().split())))

# for r in triangle:
#     print(r)

for i in range(1,n):
    for j in range(i+1):
        triangle[i][j] = triangle[i][j] + max(triangle[i-1][min(j, i-1)], triangle[i-1][max(0,j-1)])

# for r in triangle:
#     print(r)

result = 0
for i in triangle[n-1]:
    result = max( result, i )

print( result )