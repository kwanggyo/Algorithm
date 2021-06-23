# 행의 개수만큼 DFS를 돌린다.
# 방문체크한 곳들을 리스트에 1로 만든다.
import sys
sys.setrecursionlimit(1000000)

def dfs(idx, r):
    while S:
        j = S.pop()
        for k in range(N):
            if graph[j][k] == 1 and vistied[j][k] == 0:
                vistied[j][k] = 1
                S.append(k)
                path[idx][k] = '1'
                dfs(idx, k)
                vistied[j][k] = 0


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
vistied = [[0] * N for _ in range(N)]
S = []
path = [['0'] * N for _ in range(N)]

for i in range(N):
    S.append(i)
    dfs(i, i)

for j in range(N):
    print(' '.join(path[j]))

