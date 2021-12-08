# https://www.acmicpc.net/problem/1326
# 32932KB, 1080ms

from collections import deque


def bfs(s, e):
    Q = deque()
    Q.append(s-1)
    check[a-1] = 0
    while Q:
        node = Q.popleft()
        for i in range(N):
            if (i - node) % bridge[node] == 0 and check[i] == -1:
                Q.append(i)
                check[i] = check[node] + 1
                if i == e - 1:
                    return check[i]
    return -1


N = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())
ans = 10000
check = [-1] * N
print(bfs(a, b))