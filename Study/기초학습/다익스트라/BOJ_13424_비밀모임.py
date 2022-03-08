# https://www.acmicpc.net/problem/13424
# Floyd-Warshall
# 30864KB, 1636ms
# Dijkstra로 풀어보기 !

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    INF = int(1e9)
    room = [[INF] * N for _ in range(N)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        room[a - 1][b - 1] = c
        room[b - 1][a - 1] = c
    K = int(input())
    position = list(map(int, input().split()))

    # Floyd-Warshall
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    room[i][j] = 0
                    continue
                if room[i][j] > room[i][k] + room[k][j]:
                    room[i][j] = room[i][k] + room[k][j]

    ans = INF
    idx = 0
    # 어디 방이 가장 짧게 갈 수 있는지
    for i in range(N):
        tmp = 0
        for pos in position:
            tmp += room[pos-1][i]
        if ans > tmp:
            ans = tmp
            idx = i

    print(idx + 1)

