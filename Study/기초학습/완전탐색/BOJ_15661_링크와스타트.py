# https://www.acmicpc.net/problem/15661
# 145440KB, 2132ms

import sys
input = sys.stdin.readline

def cal(team):
    sum_team = 0
    for i in range(len(team)):
        for j in range(len(team)):
            if i != j:
                a, b = team[i], team[j]
                sum_team += stats[a][b]
    return sum_team


def comb(idx, start, M):
    global ans
    if idx == M:
        team1, team2 = [], []
        for i in range(N):
            if visited[i]:
                team1.append(i)
            else:
                team2.append(i)
        sum_team1 = cal(team1)
        sum_team2 = cal(team2)
        ans = min(ans, abs(sum_team1 - sum_team2))
    for j in range(start, N):
        visited[j] = 1
        comb(idx + 1, j + 1, M)
        visited[j] = 0


N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]
M = N // 2
ans = 0xffffff
visited = [0] * N
for i in range(N//2 + 1):
    comb(0, 0, i)
print(ans)
