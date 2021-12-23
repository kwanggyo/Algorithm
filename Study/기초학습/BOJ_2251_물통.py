# https://www.acmicpc.net/problem/2251
# BFS
# 32100KB, 88ms
# 경우의 수 a->b, a->c, b->c, b->a, c->a, c->b

from collections import deque

def move(x, y):
    if visited[x][y] == 0:
        visited[x][y] = 1
        Q.append((x, y))

def bfs():
    while Q:
        a, b = Q.popleft()
        c = C - a - b
        if a == 0:
            ans.append(c)
        # a -> b
        water = min(a, B - b)
        move(a - water, b + water)
        # a -> c
        water = min(a, C - c)
        move(a - water, b)
        # b -> c
        water = min(b, C - c)
        move(a, b - water)
        # b -> a
        water = min(b, A - a)
        move(a + water, b - water)
        # c -> a
        water = min(c, A - a)
        move(a + water, b)
        # c -> b
        water = min(c, B - b)
        move(a, b + water)


A, B, C = map(int, input().split())
visited = [[0] * (B + 1) for _ in range(A + 1)] # A와 B에 들어있는 물의 양으로 방문 체크
visited[0][0] = 1
ans = []
Q = deque()
Q.append((0, 0))
bfs()
print(*sorted(ans))
