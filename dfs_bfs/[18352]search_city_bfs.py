# bfs로도 풀었는데... 시간초과뜸
# 인터넷에 찾아보니 input.split()이 시간초과를 유발하니 sys.stdin.readline()를 쓰라고 한다
# 동빈쓰는 그냥 input.split 썼던데 쩝 죽어야겟다

def bfs(array, start_points, k, K ):
    # print( k, start_points)
    if k == K:
        return start_points
    elif len(start_points) > 0:
        temp = []
        for i in start_points:
            for j in array[i-1]:
                temp.append(j)
        return bfs( array, temp, k+1, K )
    else:
        return -1

def foundShorterDistance(array, start_points, target, k, K ):
    # print( k, start_points)
    if k < K and (target in start_points):
        return True
    elif k == K:
        return False
    elif len(start_points) > 0:
        temp = []
        for i in start_points:
            for j in array[i-1]:
                temp.append(j)
        return foundShorterDistance( array, temp, target, k+1, K )
    else:
        return False


N, M, K, X = map(int, input().split())

edge_list = [ [] for i in range(N) ]

for i in range(M):
    start, end = map( int, input().split() )
    edge_list[start-1].append(end)

candidate_list = bfs(edge_list, [X], 0, K)

if len(candidate_list) == 0:
    print( -1 )
else:
    for i in candidate_list:
        if(foundShorterDistance(edge_list, [X], i, 0, K) == False):
            print( i )
