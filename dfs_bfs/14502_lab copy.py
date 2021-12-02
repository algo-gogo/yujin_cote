# 문제를 완전 잘못 이해함 아놔........ 벽은 턴마다 세개가 아니라 그냥 세개만 설치함......
# 미쳤나봄...ㅡㅡ
# 하....................왠지 문제가 진짜 더럽게풀리더라....................

# 연구소 크기 N*M "직사각형"
# 한 칸은 빈칸 또는 벽 또는 바이러스. 0 빈칸 1 벽 2 바이러스
# 바이러스는 상하좌우 한칸씩 퍼져나간다.
# 벽은 꼭 세개를 세워야 한다.
# 벽으로 고립되어 바이러스가 퍼질 수 없는 곳은 안전영역
# 안전영역 크기의 최댓값...

# def candidate

from itertools import combinations

def safe_area(array):
    count = 0
    for row in array:
        temp = row.count(0)
        if temp :
            count += temp
    return count

def virus(array, current_nodes, safe_nodes):
    if len(current_nodes) == 0:
        return len(safe_nodes)

    next_nodes = []
    for i in current_nodes:
        for direction in directions:
            tempY = i[0] + direction[0]
            tempX = i[1] + direction[1]
            if N > tempY >= 0 and M > tempX >= 0:
                if array[tempY][tempX] == 0:
                    array[tempY][tempX] = 2
                    safe_nodes.remove((tempY, tempX))
                    next_nodes.append((tempY, tempX))
    return virus(array, next_nodes, safe_nodes)

def bfs(current_nodes):

    temp_safe = combinations(safe_list, 3)

    result = 0

    for item in temp_safe:
        temp_virus = [row[:] for row in lab]
        temp_safe = [row[:] for row in safe_list]
        for i in item:
            temp_virus[i[0]][i[1]] = 1
            temp_safe.remove(i)
        temp = virus(temp_virus, current_nodes, temp_safe)
        if result == 0:
            result = temp
        elif result < temp:
            result = temp
    return result

N, M = map(int, input().split())

# 상 하 좌 우
directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
virus_list = []
safe_list = []

lab = []

for row in range(N):
    lab.append(list(map(int, input().split())))
    for i in range(M):
        if( lab[row][i] == 2 ):
            virus_list.append((row, i))
        elif( lab[row][i] == 0 ):
            safe_list.append((row, i))

# for pos in safe_list:
    # safe_area([pos])
print(bfs(virus_list))
