'''combination = []

def nano_combi(array):
    if( len(array) == 0 ):
        return

    combination.append(sum(array))

    for i in range(len(array)):
        temp = list(array)
        del temp[i]
        nano_combi(temp)

def solution(array):

    print("start with : ", array)

    # for i in range(1,len(array)+1):
    nano_combi(array)

    for i in range(1,1000):
        if i not in combination:
            return i

    return -1

print(solution([3,2,1,1,9]))

print(combination, len(combination))'''

def solution(coin_list):
    coin_list.sort()

    target = 1
    for x in coin_list:
        # 만들 수 없는 금액을 찾았을 때 반복 종료
        if target < x:
            break
        target += x

    # 만들 수 없는 금액 출력
    print(target)

print(solution([3,1,1,9,8]))