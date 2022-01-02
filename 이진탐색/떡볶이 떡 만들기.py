def use_cutter(array, H ):
    total = 0

    for ddeok in array:
        if ddeok > H:
            total += ddeok-H
    
    return total

def find( array, length, start, end ):
    mid = (start + end) // 2
    temp = use_cutter(array,array[mid])
    if( temp == length ):
        return array[mid]
    elif( end-start == 0 ):
        return array[end+1] # 값이 남아서 탐색을 실패한 경우 마지막 인덱스 다음값이 답일 확률이 높지 않을까?
    elif( temp < length ):
        return find(array, length, mid+1, end)
    else:
        return find(array, length, start, mid-1)

N, M = map(int, input().split())

height_list = list(map(int, input().split()))

height_list.sort()

print(find(height_list, M, 0, N-1))