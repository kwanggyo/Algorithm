https://www.acmicpc.net/problem/2636

from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    while Q:
        return


N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
Q = deque()
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
result = []

while True:
    count = bfs()
    if count == 0:
        break
    result.append(count)

print(result[-1])