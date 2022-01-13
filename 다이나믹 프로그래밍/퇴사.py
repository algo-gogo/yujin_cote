'''
퇴사하는 백준이
N+1일에 퇴사하기 위해 N일동안 최대한 많이 일하는 성실한아이
비서도있는 백준이
하루에 하나씩 서로 다른 사람의 상담
상담 완료하는데걸리는 시간과 받는 금액.
최대수익을 구해야한다
'''

N = int(input())
task = []

d = [0] * (N+1)

for i in range(N):
    task.append(list(map(int, input().split())))

'''
0 1 2 3 4 5 6
0 -> 불가능
0 1 -> 불가능
0 1 2 -> 2는 가능

0
0
1
0 1
'''
# for i in range(1,N+1):
#     for j in range(0, i): #0부터시작.
#         if j + task[j][0] < i:
#             d[i] = max(d[i], d[i] + task[j][1])
#             j += task[j][0]

#         print(i, j, d[i])

max_result = 0

for day in range(1, N+1):
    for i in range(day):
        temp = i
        print("day - ", day, task[i])
        if i + task[i][0] <= day:
            d[day] += task[i][1]
            temp += task[i][0]

print(task)
print(d)

# 0 0 10 40