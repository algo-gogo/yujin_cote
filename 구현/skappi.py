'''
n은 총 둘레. 0~n-1까지의 범위가 있는 셈
시계방향, 반시계방향으로 이동 가능
dist는 한 사람이 움직일 수 있는 거리
출발지점 정해진게없음
'''

def solution(n, weak, dist):
    answer = 0

    dist.sort() # 앞에있는거부터 처리해야지

    count = 0

    parts = []
    
    for start in range(len(weak)):
        left = start - 1
        if left < 0 : left = len(weak)-1
        right = start + 1
        if right == len(weak) : right = 0

        left_distance = weak[start]-weak[left]
        if left_distance < 0 : left_distance = -1*n - left_distance
        right_distance = weak[right]-weak[start]
        if right_distance < 0 : right_distance = -1*n - right_distance

        if left_distance < right_distance :
            parts.append((left_distance, weak[left],weak[start]))
        else:
            parts.append((right_distance, weak[start],weak[right]))

        print(weak[start], left_distance, right_distance)


    parts = list(set(parts))
    print(parts)

    answer = -1

    for person in dist:
        current_index = 0
        for part in range(len(parts)):
            current_index = parts[part][1]
            if abs(parts[part][0]) < person:
                current_index = current_index+person
                if current_index >= n:
                    current_index -= n
                    print(person, parts[part], current_index)
                    del parts[part]
                    part = part - 1
                    continue
            else:
                break



    return answer

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))