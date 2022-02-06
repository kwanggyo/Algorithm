# https://www.acmicpc.net/problem/16953
# BFS
# 32904KB, 156ms

from collections import deque

def bfs(n):
    Q = deque()
    Q.append((n, 1))
    while Q:
        number, cnt = Q.popleft()
        if number == B:
            return cnt
        if number > B:
            continue
        else:
            Q.append((number * 2, cnt + 1))
            Q.append((int(str(number) + '1'), cnt + 1))
    return -1

A, B = map(int, input().split())
print(bfs(A))