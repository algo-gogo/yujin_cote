'''
집 N개가 수직선 위에 있다.
집 여러개가 같은 좌표를 가지지는 않는다.
C개의 공유기를 온갖집에 설치한다.
가장 인접한 두 공유기 사이의 거리를 최대로

end값은 와이파이 개수의 비율에 반비례한다.
개수가 클 수록 쓸데없이 표본을 줄이는 과정을 겪을 필요는 없다
개수가 적을 수록 끄트머리부터 계산해야한다(2개면 한쪽끝과 반대쪽 끝지점임)

5개중의 3개라면
60퍼는 날려도 되나?
1 2 4 8 9
날리면 1이랑 2밖에ㅔ안남는데..
4를 고르게하는방법은?
60퍼를날리고 +1?
5 * ((5-3) / 5) ??
'''

from math import floor

def solution(house_list, wifi_list, house_count, wifi_count):
    # end = house_count-1 - (house_count-house_count//(wifi_count-1)) # 와이파이 숫자가 작거나 아예 집개수와 같으면 효과적인데 과반수가 되는경우 망함
    end = floor(house_count * ((house_count-(wifi_count-1)) / house_count))
    while( True ):
        # print("end: ", end)
        wifi_list = []
        last_wifi = None
        min_term = 1000000000
        # term = (house_count)//wifi_count
        # term = (house_list[end]+house_list[0])//2-house_list[0] # 가장 근접했던거같긴한데 2개일때 문제가 생김.
        # term = (house_list[end]-house_list[0])//(house_count-house_count//(wifi_count-1)+1)
        term = house_list[end]-house_list[0]
        # print("term: ",term)
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
            end = end - 1 # 되긴하는데 시간이 초과됨. 좀 더 효율적인 방법은?
            #end = end - (house_count//(end+1))
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

5 5
1
100
30000
3
40

3 3
1
3
4

3 3
1
4
6

5 3
1
7
8
9
10

5 2
1
7
8
9
10

10 3
1
2
4
7
11
16
22
29
37
46
'''