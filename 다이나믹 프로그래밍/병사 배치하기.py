'''
N명의 병사가 무작위로
전투력이있음
전투력이 높은 순서부터 내림차순
남아있는 병사의 수가 최대
'''

N = int(input())
d = [0] * N

soldier_list = list(map(int, input().split()))

soldier_list.reverse()

d[0] = 1

# print( soldier_list )

for i in range(1,N):
    if soldier_list[i] < soldier_list[i-1]:
        d[i] = d[i-1]
        flag = False
        for j in range(i-1):
            if soldier_list[j] < soldier_list[i]:
                flag = True
            else:
                flag = False
                soldier_list[i] = soldier_list[i-1]

        if flag:
            soldier_list[i-1] = soldier_list[i]


    else:
        d[i] = d[i-1] +1

    # print( soldier_list )
    # print( d )

print(N-d[N-1])

'''
7
15 11 4 8 5 2 4

7
15 11 4 1 5 2 4

5
1 2 3 4 5

1
1

5
6 1 5 1 4
'''