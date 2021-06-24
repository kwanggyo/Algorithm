# 행의 개수만큼 DFS를 돌린다.
# 방문체크한 곳들을 리스트에 1로 만든다.

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 플로이드-워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            if not graph[i][j] and graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(N):
    res = ''
    for j in range(N):
        res += str(graph[i][j]) + ' '
    print(res)

