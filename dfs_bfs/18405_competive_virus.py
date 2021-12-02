'''
쉽다
!!!!!
아마도!!!?!@?!!?@?
3 3 -> N행열 K개
1 0 2
0 0 0
3 0 0   -> 초기세팅
2 3 2   -> S, X, Y S초 뒤에 X행 Y열, -1해야함
'''

def virus(virus_list, count):
    left = 0
    for row in virus_list:
        left += len(row)
    if(count == S or left == 0):
        return

    next_list = [[] for row in range(K)]

    for virus_type in range(len(virus_list)):
        for item in virus_list[virus_type]:
            for direction in directions:
                tempX = item[0]+direction[0]
                tempY = item[1]+direction[1]
                if N > tempY >= 0 and N > tempX >= 0:
                    if field[tempX][tempY] == 0:
                        field[tempX][tempY] = virus_type+1
                        next_list[virus_type].append((tempX,tempY))
    return virus(next_list, count+1)

directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
N, K = map(int, input().split())

field = []
virus_list = [[] for row in range(K)]

for row in range(N):
    field.append(list(map(int, input().split())))
    for i in range(N):
        if field[row][i]:
            virus_list[field[row][i]-1].append((row, i))

S, X, Y = map(int, input().split())

virus(virus_list, 0)

print(field[X-1][Y-1])