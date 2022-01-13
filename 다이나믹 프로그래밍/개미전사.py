'''
일직선상에 식량창고가 있음
메뚜기들은 인접한 창고가 공격받으면 알 수있음
한칸이상 떨어진 창고를 약탈해야함.
'''

N = int(input())
K = list(map(int,input().split()))

d = [0] * 101

d[1] = K[0]
d[2] = max(K[1],K[0])

for i in range(2, N+1):
    d[i] = max(d[i], d[i-2]+K[i-1])

    print(d[1:10])

print(d[N])