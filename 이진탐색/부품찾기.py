def find( array, finds, size ):
    for find in finds:
        if binary(array, find, 0, size-1) == False:
            return "no"
    return "yes"

def binary(array, find, start, end):
    mid = (start + end) // 2

    if( array[mid] == find ):
        return True
    elif( end-start == 0 ):
        return False
    elif( array[mid] < find ):
        return binary(array, find, mid+1, end)
    else:
        return binary(array, find, start, mid-1)

N = int(input())
part_list = list(map(int,input().split()))
M = int(input())
find_list = list(map(int,input().split()))

part_list.sort()
find_list.sort()

print(find(part_list, find_list, N))
