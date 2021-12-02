# bfs로도 풀었는데... 시간초과뜸
# 인터넷에 찾아보니 input.split()이 시간초과를 유발하니 sys.stdin.readline()를 쓰라고 한다
# 동빈쓰는 그냥 input.split 썼던데 쩝 죽어야겟다

def bfs(array, current_nodes, k, K ):
    if k == K:
        return current_nodes
    elif len(current_nodes) > 0:
        next_nodes = []
        for i in current_nodes:
            for j in array[i-1]:
                if dist_list[j-1] == None:
                    next_nodes.append(j)
                    dist_list[j-1] = k

        return bfs( array, next_nodes, k+1, K )
    else:
        return -1

N, M, K, X = map(int, input().split())

edge_list = [ [] for i in range(N) ]
dist_list = [ None ] * N

for i in range(M):
    start, end = map( int, input().split() )
    edge_list[start-1].append(end)

candidate_list = bfs(edge_list, [X], 0, K)

if len(candidate_list) == 0:
    print( -1 )
else:
    for i in candidate_list:
        print(i)
