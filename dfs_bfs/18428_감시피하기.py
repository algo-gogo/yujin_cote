'''
문제읽기타임
NxN크기의 복도따리복도따
선생님, 학생, 장애물
선생님들은 상 하 좌 우 네방향 감시. 장애물 뒷부분은 진행 불가 대각선도 불가
딱 세개만 설치 가능.
모든 학생을 숨길 수 있는지 계산. -> 선생이랑 딱붙어있는 경우는 아예불가능하겠는데?

설치 가능 여부를 묻는 거니까 꼭 설치를 할 필요는 없지 않을까?
선생님이 한줄에 겹치는경우는 어떻게 카운트하지?
'''

from itertools import combinations

N = int(input())

corridor = []
teachers = []
blanks = []

for i in range(N):
    temp = list(input().split())
    corridor.append(temp)
    for j in range(N):
        if( temp[j] == 'T' ):
            teachers.append((i, j))
        elif( temp[j] == 'X' ):
            blanks.append((i, j))

# print(teachers)

directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]

def find_student(array, next_sight, candidate):
    if( next_sight == None ) :
        next_sight = []
        for teacher in teachers:
            for direction in directions:
                next_sight.append((teacher, direction))
    elif len(next_sight) == 0:
        return False

    next_nodes = []
    for i in next_sight:
        tempI = i[0][0] + i[1][0]
        tempJ = i[0][1] + i[1][1]
        if N > tempI >= 0 and N > tempJ >= 0:
            if array[tempI][tempJ] == 'X':
                if not (tempI, tempJ) in candidate:
                    next_nodes.append(((tempI, tempJ), (i[1][0], i[1][1])))
            elif array[tempI][tempJ] == 'S':
                return True
    return find_student(array, next_nodes, candidate)


def solution():
    candidates = combinations(blanks, 3)

    for candidate in candidates:
        if( find_student(corridor, None, candidate) == False ):
            return "YES"
    return "NO"

print(solution())

'''
4
S S S X
X X X X
X X X X
X X X X

4
X S X T
X X S X
X X X X
T T T X

5
X X S X X
X X X X X
S X T X S
X X X X X
X X S X X

'''