'''
N*M 크기의 금광. 각 칸은 금이있고
채굴자는 첫번째 열부터 금을 캐기시작
어느행에서든 출발할 수 있음
M번에 걸쳐서 오른쪽 위, 오른쪽, 오른쪽 아래의 위치로 이동
금의 최대크기
'''

T = int(input())

result = [0] * T

for t in range(T):
    N, M = map(int, input().split())

    gold = list(map(int, input().split()))

    # for r in range(M-1):
    #     print( gold [r*M:(r+1)*M] )

    d = [[0] * M for i in range(N)]

    for i in range(N):
        d[i][0] = gold[i*M]

    for j in range(1, M):
        for i in range(N):
            d[i][j] = gold[i*M+j] + max(d[i][j-1], d[min(N-1,i+1)][j-1], d[max(i-1,0)][j-1])

    # for r in d:
    #     print(r)

    for i in range(N):
        result[t] = max(result[t], d[i][M-1])


for r in result:
    print( r )
