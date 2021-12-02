def rotate90(position_list, size):
    result = []
    for position in position_list:
        result.append((position[1],size-position[0]))
    return result

def solution(key, lock):
    print("자물쇠 값")
    print('='*10)
    for row in lock:
        print(row)

    print()
    print("열쇠 값")
    print('='*10)
    for row in key:
        print(row)

    # 빈칸의 위치를 파악하기
    # 전부 값을 반전시켜봐야하나?

    # 열쇠의 기대값 -> lock 반전
    # 1값의 위치를 받아야 하나???모르겠다진짜...

    position_list = []

    for y in range(len(lock)):
        for x in range(len(lock[y])):
            if lock[y][x] == 1:
                lock[y][x] = 0
            else:
                position_list.append((y, x))
                lock[y][x] = 1

    print()
    print("열쇠의 기대값")
    print('='*10)
    for row in lock:
        print(row)

    # print()
    # print("홈 위치들 아놔 짱나")
    # print('='*10)
    # print(position_list)

    key_position = []
    for y in range(len(key)):
        if key[y].count(1):
            for x in range(len(key[y])):
                if key[y][x] == 1:
                    key_position.append((y, x))

    key_size = len(key[0])
    lock_size = len(lock[0])

    # print()
    # print("열쇠 돌기 위치들 아놔 짱나")
    # print('='*10)
    # print(key_position)

    degree = 0

    current_key = key_position

    # 회전하는 경우? 다행히 key는 정사각형임 아놔시발진짜짱나네
    # 회전행렬ㄹ????은개오바인듯
    # 회전행렬기준 90도회전하는 좌표 -> x=rowsize-y, y=x

    if len(position_list) > len(key_position):
        return False
    elif len(position_list) == 0:
        return True

    accepted_count = 0
    while degree < 360:
        #챌린지
        accepted_count = 0
        for hom in position_list:
            for dolgi in current_key:
                #위치 보정
                offset_y = hom[0] - dolgi[0]
                offset_x = hom[1] - dolgi[1]

                # 되는지 체크
                dolgi_exists = True
                for check in current_key:
                    if 0 <= check[0]+offset_y < lock_size and 0 <= check[1]+offset_x < lock_size:
                        if position_list.count((check[0]+offset_y, check[1]+offset_x)) == 0:
                            dolgi_exists = False

                # lock[dolgi[0]+offset_y][dolgi[1]+offset_x]
                # 바운더리 체크
                # 범위 안에는 있지만 남는경우??

                if dolgi_exists == False:
                    continue
                else:
                    accepted_count += 1
                    break # 바로 다음 이동. ?

        # 성공 여부 체크
        if accepted_count == len(position_list):
            return True
        current_key = rotate90(current_key, key_size)
        degree += 90

    return False

print(solution(
    [[0, 0, 0], [1, 0, 0], [0, 1, 1]],
    [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    ))
