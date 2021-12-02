#초안

#일단 원형큐 삥글뺑글
#시작한지 K초 후 중단
#다시 회복 X초 -> 상관없는 값
#K초 시점에서 가리키는 위치 리턴.

def solution(food_times, k):
    length = len(food_times)
    
    remain_foods = list(range(0, length))
    timestamp = 0
    
    current_index = 0
    
    while timestamp < k:
        food_times[remain_foods[current_index]] = food_times[remain_foods[current_index]]-1
        
        timestamp += 1
        
        if( food_times[remain_foods[current_index]] <= 0 ):
            del remain_foods[current_index]
            length = length - 1
            if length == 0:
                return -1
            current_index -= 1
        if current_index+1 < length:
            current_index = (current_index + 1)
        else:
            current_index = 0
            
    return remain_foods[current_index] + 1