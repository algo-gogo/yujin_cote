'''
고정점이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미합니다.
하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며,
모든 원소가 오름차순으로 정렬되어 있습니다.
이때 이 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램을 작성하세요.
고정점은 최대 1개만 존재합니다. 만약 고정점이 없다면 -1을 출력합니다.

입력 예시 1
5
-15 -6 1 3 7
답:3

입력 예시 2
7
-15 -4 2 8 9 13 15
답:2

입력 예시 3
7
-15 -4 3 8 9 13 15
답:-1
'''

def fixed_index(array, start, end ):
    mid = (start + end) // 2

    if( start>end ):
        return -1
    elif( array[mid] == mid ):
        return mid
    elif( array[mid] < mid ):
        return fixed_index(array, mid+1, end)
    else:
        return fixed_index(array, start, mid-1)

N = int(input())
permutation = list(map(int,input().split()))

print( fixed_index(permutation, 0, N-1) )