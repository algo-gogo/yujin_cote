'''
N*N크기의 땅
각 땅에는 나라가 하나씩 있대
r행 c열에는 A[r][c]명이 살고잇음
국경선이있음
인구이동 ㄱ ㄱ
인구이동이 없을때까지 매일반복
1. 두 나라의 인구차이가 L명 이상 R명 이하면 하루동안 엶
2. 인구이동 ㄱ ㄱ ㄱ
3. 인접한 칸만을 이용해 이동할 수 있으면???붙어있단말인가???하루동안 연합
4. 연합을 이루는 인구들은 평균치로 계산하며 소수점 ㅂ2 남는 한명은 반으로 쪼개진거임???
5. 연합을 해체하고 국경을 닫는다 -> 걍 평균치로맞춰버린다는뜻인가?

목표
우선 연합을 한번만 시켜보자

목표2
각 노드마다 주변의 연합가능여부를 체크한다음.
연합한 노드를 리스트로 갖고.
dfs로 쫙 돌려서 연합한애들을 계산하면 될거같기도 하다.,,아닌가 모르겟음ㅋ눈물난다
'''

from math import floor

directions = ((0,1), (0,-1), (1,0), (-1,0))

N, L, R = map(int, input().split())

def dfs(graph, r, c, visited, united):
    if visited[r][c] == True:
        return united
    visited[r][c] = True
    united.append((r,c))
    # print( r,c, graph[r][c], visited )
    # print(total)

    for i in graph[r][c]:
        # print( i )
        if not visited[i[0]][i[1]]:
            dfs(graph, i[0], i[1], visited, united)

    # print(united)
    return united
    

def unite(array, r, c):
    unite_list = []

    for d in directions:
        tempR = r+d[0]
        tempC = c+d[1]
        if N > tempR >= 0 and N > tempC >= 0:
            if R >= abs(array[tempR][tempC] - array[r][c]) >= L:
                unite_list.append((tempR, tempC))
    
    if len(unite_list) > 0:
        return unite_list
    else:
        return []


A = []
for row in range(N):
    A.append(list(map(int, input().split())))

# for r in range(N):
#     print(A[r])

day_count = 0

while True:
    unite_graph = [[] for i in range(N)]
    visited = [[False] * (N) for i in range(N)]

    unite_count = 0
    for r in range(N):
        for c in range(N):
            unite_graph[r].append(unite(A, r,c))
            if len(unite_graph[r][c]) > 0:
                unite_count += 1

    if( unite_count == 0 ):
        break

    for r in range(N):
        for c in range(N):
            temp = dfs(unite_graph, r, c, visited, [])
            if( len(temp) > 0 ):
                total = 0
                for i in temp:
                    total = total + A[i[0]][i[1]]

                value = floor(total / len(temp))
                for i in temp:
                    A[i[0]][i[1]] = value

    # for r in range(N):
    #     print(A[r])
    
    day_count += 1

print( day_count )


# print(dfs(unite_graph, 0, 0, visited, []))