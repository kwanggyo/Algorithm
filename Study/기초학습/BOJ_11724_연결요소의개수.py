# https://www.acmicpc.net/problem/11724
# 63768KB, 788ms

import sys
sys.setrecursionlimit(10000)    # 파이썬 최대 재귀 횟수(1000회) 수정
input = sys.stdin.readline      # 이 부분 없으면 시간초과

def dfs(v):
    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            dfs(w)


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 0
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)