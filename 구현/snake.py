'''
뱀은 초마다 이동. 맨위맨좌측부터.
처음엔 오른쪽으로 이동.
이동할 때 꼬리 가만히있고 머리를 이동.
사과가 있으면 길이 유지. 없으면 원래 길이로 돌아옴.
벽 또는 자신과 부딪히면 끝.

.... 0부터 시작하는거 아님 황당하게 삽질했음 글자를 좀 똑바로 읽자
'''

size = int(input())
map_array = [[0] * (size) for i in range(size)]

# 편의를 위해 X,Y순
snake = [(0,0)]

apple_count = int(input())

for i in range(apple_count):
    position = list(map(int, input().split()))
    map_array[position[0]-1][position[1]-1] = 1

turn_count = int(input())

turn_list = []

for i in range(turn_count):
    temp = input().split()

    turn_list.append((int(temp[0]), temp[1]))
turn_list.sort()

print(turn_list)

move_x = 1
move_y = 0

t = 0
while(True):
    print("STAGE : ", t)
    for row in map_array:
        print(row)
    print(snake[0][0], snake[0][1])

    current_x = snake[0][0] + move_x
    current_y = snake[0][1] + move_y

    t += 1

    if( len(turn_list) > 0 and t == turn_list[0][0] ):
        if( turn_list[0][1] == 'L' ):
            temp = move_x
            move_x = move_y
            move_y = -temp
        else:
            temp = move_y
            move_y = move_x
            move_x = -temp
        turn_list.pop(0)

    if( 0<=current_x<size and 0<=current_y<size ):
        if( snake.count((current_x,current_y)) > 0 ):
            break
        snake.insert(0,(current_x,current_y))

        if( map_array[current_y][current_x] == 1 ):
            map_array[current_y][current_x] = 0
        else:
            snake.pop()
    else:
        break

print(t)
print(snake)


'''
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 0, 1, 1, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''