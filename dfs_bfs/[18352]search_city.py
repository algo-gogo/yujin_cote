# 문제는 풀었는데 시간초과
# 그냥 별생각없이 DFS로 햇음..

# 1~N번까지 노드, M개의 간선
# 모든 간선 가중치 1
# 도시 X로부터 출발해서 도달할 수 있는 모든 도시 중 최단거리가 정확히 K인 모든 도시들의 번호
# 출발지 그대로는 0

def dfs(current, array, k):
    if( k == K ):
        candidate_list.append(current)
    # print( current, array[current-1], k )
    if len(array[current-1]):
        for next_node in array[current-1]:
            dfs(next_node, array, k + 1)

def findShortest(start, end, array, k, K):
    if( start == end and k < K ):
        return True
    elif len(array[start-1]):
        for next_node in array[start-1]:
            if findShortest(next_node, end, array, k + 1, K):
                return True

N, M, K, X = map(int, input().split())

edge_list = [ [] for i in range(N) ]

for i in range(M):
    start, end = map( int, input().split() )
    edge_list[start-1].append(end)

candidate_list = []

k = 0
current_node = X
dfs(current_node, edge_list, k)

if( len(candidate_list) == 0 ):
    print( -1 )

for i in candidate_list[:]:
    if(findShortest(X, i, edge_list, 0, K) != True):
        print(i)
