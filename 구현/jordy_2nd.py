'''
1. 맵 만들기 (이게 제일 쉬운 접근인듯)

'''

def bo_available(map_array, n, target_x, target_y):
    check_list = []
    if target_x == 0:
        check_list.append((target_x+1, target_y))
    elif target_x == n:
        check_list.append((target_x-1, target_y))
    else:
        check_list.append((target_x+1, target_y))
        check_list.append((target_x-1, target_y))

    for i in check_list:
        x = i[0]
        y = i[1]
        left = max(x-1,0)
        right = min(x+1,n)
        under = max(y-1,0)
        if map_array[y][x] == 1:
            if map_array[under][x] == 0 or map_array[under][right] == 0:    # 한쪽 끝이 기둥에, 즉 밑에 또는 우하단에 기둥이 있는 경우
                map_array[y][x] = 1
                continue
            elif (map_array[y][left] == 1 and map_array[y][right] == 1):    # 양쪽 끝에 보가 있음
                map_array[y][x] = 1
                continue
        elif map_array[y][x] == 0:
            if y == 0 or map_array[under][x] == 0:    # 바닥에 있거나, 다른 기둥 위에
                continue
            elif map_array[y][left] == 1:           # 보의 한쪽 끝 위에, 좌측이 보인 경우만 가능. (우측에 보가 있으려면 겹친다.)
                continue
        else:
            continue
        return False
    return True

    


def solution(n, build_frame):
    map_array = [[None] * (n+1) for i in range(n+1)]
    answer = []

    for stage in build_frame:
        x = stage[0]
        y = stage[1]
        is_bo = stage[2]
        is_new = stage[3]
        left = max(x-1,0)
        right = min(x+1,n)
        under = max(y-1,0)
        top = min(y+1,n)

        if is_new == 1:
            if is_bo:
                if y == 0:
                    continue
                elif map_array[under][x] == 0 or map_array[under][right] == 0:    # 한쪽 끝이 기둥에, 즉 밑에 또는 우하단에 기둥이 있는 경우
                    map_array[y][x] = 1
                    answer.append([x,y,is_bo])
                elif (map_array[y][left] == 1 and map_array[y][right] == 1):    # 양쪽 끝에 보가 있음
                    map_array[y][x] = 1
                    answer.append([x,y,is_bo])
            else:
                if y == 0 or map_array[under][x] == 0:    # 바닥에 있거나, 다른 기둥 위에
                    map_array[y][x] = 0
                    answer.append([x,y,is_bo])
                elif map_array[y][left] == 1:           # 보의 한쪽 끝 위에, 좌측이 보인 경우만 가능. (우측에 보가 있으려면 겹친다.)
                    map_array[y][x] = 0
                    answer.append([x,y,is_bo])
        else:
            want_to_remove = [x,y,is_bo]

            if( want_to_remove not in answer ):
                continue
            delete_index = answer.index(want_to_remove)

            if is_bo: # 삭제 시 좌우측이 만족해야 한다.
                map_array[y][x] = None
                if bo_available(map_array, n, x, y):
                    del answer[delete_index]
                else:
                    map_array[y][x] = 1
            else:   # 기둥이 지워지는 조건
                if map_array[top][x] == None and map_array[top][left] != 1:     # 위에 뭐가 얹어지지 않은 상황.
                    del answer[delete_index]
                    map_array[y][x] = None
                elif map_array[top][x] == 0 and map_array[top][left] == 1:      # 위에 기둥이 있고 좌상단에 보가 있는 경우엔 이미 이어져있으므로 ㄱㅊ.
                    del answer[delete_index]
                    map_array[y][x] = None
                elif map_array[top][x] == 1 and map_array[top][left] == 1:      # 위에 보가 있고 왼쪽에도 보가 있으면 이미 연결된걸로 간주.
                    del answer[delete_index]
                    map_array[y][x] = None

    answer.sort()
    return answer

print(solution(100,  [[2, 0, 0, 1], [100, 0, 0, 1], [100, 1, 1, 1], [99, 1, 1, 1], [99, 1, 0, 1], [99, 0, 0, 1],[2, 1, 0, 1],[2, 2, 0, 1],[2, 2, 1, 1]]
))
#[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
#[[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]