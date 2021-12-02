'''죄송 저 이거 풀다가 포기했습니다 접근법을 바꾸고 처음부터 다시 풀어서 갱신할게요'''

def is_able(size, field, stage):
    print(stage)

    x = stage[0]
    y = stage[1]

    near = []

    index = 0

    # if stage[2] == 1 and stage[1]==0:
        # return -1

    for row in range(len(field)):
        if field[row][0] == stage[0] and field[row][1] == stage[1]:
            if( stage[3] ):
                return -1
            elif field[row][2] == stage[2]:
                index = row
                continue
            return -1
        elif abs(field[row][0] - stage[0]) == 1 and abs(field[row][1] - stage[1]) == 1:
            near.append(field[row])

    for row in near:
        if row[0] > stage[0] and row[2] == 0:
            return -1
        elif row[1] > stage[1] and row[2] == 1:
            return -1

    if( stage[3] == 0 ):
        return index

    

def solution(n, build_frame):
    answer = []
    
    for stage in build_frame:
        x = stage[0]
        y = stage[1]
        build_type = stage[2] # 0 is pillar, 1 is floor
        is_build = stage[3]
        result = is_able(n, answer, stage)
        if result != -1:
            if( is_build ):
                row = len(answer)
                for i in range(len(answer)):
                    if answer[i][0]*10+answer[i][1] >= x*10+y :
                        row = i
                        break
                answer.insert(row,[x, y, build_type])
            else:
                print(result)
                del answer[result]
    
    return answer

print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))