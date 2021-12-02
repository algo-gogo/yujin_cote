#일단 원형큐 삥글뺑글
#시작한지 K초 후 중단
#다시 회복 X초 -> 상관없는 값
#K초 시점에서 가리키는 위치 리턴.

def solution(food_times, k):
    length = len(food_times)
    total = sum(food_times)

    print(total)

    if total <= k:
        return -1
    elif length > k:
        return k

    timestamp = 0
    
    while( timestamp < k ):
        smallest = min(food_times)
        count_round = int((k-timestamp) / length)
        count_remain = int((k-timestamp) % length)

        print('*'*20)
        print("smallest : ", smallest)
        print("round :", count_round)
        print("mod : ", count_remain)

        if( smallest > count_round ):
            return (length % (k+1-timestamp)) - 1
        else:
            delete_index = food_times.index(smallest)
            print("delete index :", delete_index)
            timestamp = timestamp + delete_index + (length * (smallest-1))
            print(timestamp)
            del food_times[delete_index]
            length = length-1
        

    



print(solution([3, 1, 2], 3))