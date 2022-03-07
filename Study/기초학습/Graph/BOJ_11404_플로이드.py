# https://www.acmicpc.net/problem/11404
# Floyd-Warshall
# 30864KB, 524ms

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)
city = [[INF] * (N) for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    # 노선이 여러개 있는 경우 비용이 제일 적게 드는 것을 넣어준다.
    if city[a-1][b-1] > c:
        city[a - 1][b - 1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if city[i][j] > city[i][k] + city[k][j]:
                city[i][j] = city[i][k] + city[k][j]

# 갈 수 없는 곳은 0으로
for i in range(N):
    for j in range(N):
        if city[i][j] == INF:
            city[i][j] = 0
    print(' '.join(map(str, city[i])))
