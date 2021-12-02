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

from itertools import combinations

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
chicken_combi = combinations(chicken_position, max_chicken)

min_value = 0
for combi in chicken_combi:
    city_chicken = 0
    for house in house_position:
        chicken_distance = 0
        for store in combi:
            temp = abs(store[0]-house[0])+abs(store[1]-house[1])
            if chicken_distance != 0 and chicken_distance < temp:
                continue
            chicken_distance = temp
        city_chicken += chicken_distance
    if min_value == 0 or min_value > city_chicken:
        min_value = city_chicken
    
print(min_value)