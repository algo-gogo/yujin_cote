'''
공배수를 구하는 느낌인건지??

동전이 2 / 3 이렇게 있다고 치고
5인 경우 2, 3
8인 경우 2, 3, 3
'''

N, M = map(int, input().split())

value_list = []
for i in range(N):
    value_list.append(int(input()))

count_list = [10001] * 10001

for i in range(M+1):
    temp = i
    count = 0
    for v in value_list:
        if count_list[i-v] != -10001:
            count_list[i] = min(count_list[i], count_list[i-v] + 1)

    count_list[i] = temp if temp != M+1 else 10001

print( count_list[1:M] )