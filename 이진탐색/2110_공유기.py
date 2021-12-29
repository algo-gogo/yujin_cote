'''
집 N개가 수직선 위에 있다.
집 여러개가 같은 좌표를 가지지는 않는다.
C개의 공유기를 온갖집에 설치한다.
가장 인접한 두 공유기 사이의 거리를 최대로
'''

def solution(house_list, wifi_list, house_count, wifi_count):
    last_wifi = None
    term = (house_list[house_count-1]-house_list[0])//wifi_count
    min_term = 1000000000
    for i in range(house_count):
        if last_wifi == None:
            last_wifi = i
        elif house_list[i] - house_list[last_wifi] < term:
            continue
        else:
            min_term = min(min_term, house_list[i]-house_list[last_wifi])
            last_wifi = i
        wifi_list.append(house_list[i])
        print(wifi_list)

        if len(wifi_list) == wifi_count:
            break

    return min_term

N, C = map(int, input().split())

x = []

for i in range(N):
    x.append(int(input()))

x.sort()
wifi_list = []
print(solution(x, wifi_list, N, C))