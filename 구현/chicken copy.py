'''
N*N 크기의 도시
1*1크기의 칸으로 되어있다
빈칸 치킨집 집 중 하나
인덱스는 1부터 시작 !!
치킨거리 이지랄
하......
치킨거리 = 제일가까운치킨집
abs(x1-x2) + abs(y1-y2)
도시의 치킨거리 = 모든집 치킨거리의 합

치킨집을 폐업시킨대 어이없네
최대 M개만 고르고 나머지 줄폐업 (M개는 주어짐)
모두를 만족하는 치킨거리를 유지하는 조건 내에서, 치킨거리의 최솟값 출력.

먼소리고이게
'''

parameter = list(map(int, input().split()))
size = parameter[0]
chicken_position = []
house_position = []

for i in range(size):
    temp = list(map(int, input().split()))
    for j in range(size):
        if temp[j] == 1:
            house_position.append((i,j))
        elif temp[j] == 2:
            chicken_position.append((i,j))

max_chicken = parameter[1]
chicken_value = []

for store in chicken_position:
    chicken_distance = 0
    nearest = 0
    for house in house_position:
        temp = (abs(store[0]-house[0])+abs(store[1]-house[1]))
        if nearest == 0 or nearest > temp:
            nearest = temp
        chicken_distance += temp

    # 전체 거리의 합 기준 제일 작은거부터
    if len(chicken_value) == 0 or chicken_value[len(chicken_value)-1][0] < chicken_distance:
        chicken_value.append((chicken_distance, store, nearest))
    elif chicken_value[0][0] > chicken_distance:
        chicken_value.insert(0, (chicken_distance, store, nearest))
    else:
        for i in range(len(chicken_value)):
            if chicken_value[i][0] == chicken_distance and chicken_value[i][2] >= nearest:
                chicken_value.insert(i, (chicken_distance, store, nearest))
            elif chicken_value[i][0] > chicken_distance:
                chicken_value.insert(i, (chicken_distance, store, nearest))
                break


    print(chicken_value)

# print(chicken_value)

chicken_value = chicken_value[0:max_chicken]

print(chicken_value)

city_chicken = 0
for house in house_position:
    chicken_distance = 0
    for store in chicken_value:
        temp = abs(store[1][0]-house[0])+abs(store[1][1]-house[1])
        if chicken_distance != 0 and chicken_distance < temp:
            continue
        chicken_distance = temp
    city_chicken += chicken_distance
    print(chicken_distance)

print(city_chicken)
