'''
집 N개가 수직선 위에 있다.
집 여러개가 같은 좌표를 가지지는 않는다.
C개의 공유기를 온갖집에 설치한다.
가장 인접한 두 공유기 사이의 거리를 최대로
'''

def solution(house_list, wifi_list, house_count, wifi_count):
    end = house_count-1
    while( True ):
        wifi_list = []
        last_wifi = None
        min_term = 1000000000
        # term = (house_count)//wifi_count
        # term = (house_list[end]-house_list[0])//2
        term = house_list[end]-house_list[0]
        # term = sum(house_list) // house_count - house_list[0]
        # term = house_list[((house_count)//2-1)]
        for i in range(house_count):
            if last_wifi == None:
                last_wifi = i
            elif (house_count-i)+len(wifi_list) < wifi_count:
                break
            elif (house_list[i] - house_list[last_wifi]) < term:
                continue
            else:
                min_term = min(min_term, house_list[i]-house_list[last_wifi])
                last_wifi = i
            wifi_list.append(house_list[i])
            # print(wifi_list)

            if len(wifi_list) == wifi_count:
                break

        if len(wifi_list) == wifi_count:
                break
        else:
            end = end // 2

    return min_term

N, C = map(int, input().split())

x = []

for i in range(N):
    x.append(int(input()))

x.sort()
wifi_list = []
print(solution(x, wifi_list, N, C))

'''
5 3
1
2
8
4
9

3 3
1
10
100

4 3
11
13
16
18

4 3
1
3
7
8 

5 3
1
7
8
9
10

5 5
1
100
30000
3
40
'''