'''
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다.
이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
단, 이 문제의 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받습니다.

오름차순이다. 그러면 start지점과 end지점을 찾으면 되지않을까
'''

def find_start(array, x, start, end, last=-1):
    mid = (start + end) // 2

    if( start>end ):
        return last
    elif( array[mid] == x ):
        last = mid
        return find_start(array, x, start, mid-1, last)
    elif( array[mid] < x ):
        return find_start(array, x, mid+1, end, last)
    else:
        return find_start(array, x, start, mid-1, last)

def find_end(array, x, start, end, last=-1):
    mid = (start + end) // 2

    if( start>end ):
        return last
    elif( array[mid] == x ):
        last = mid
        return find_end(array, x, mid+1, end, last)
    elif( array[mid] < x ):
        return find_end(array, x, mid+1, end, last)
    else:
        return find_end(array, x, start, mid-1, last)


N, x = map(int, input().split())
values = list(map(int, input().split()))
visited = [-1, -1]

start = find_start(values, x, 0, N-1)
end = find_end(values, x, 0, N-1)

print( end-start+1 )