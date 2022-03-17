# https://www.acmicpc.net/problem/15486
# DP

import sys
input = sys.stdin.readline

N = int(input())
T, P = [], []
dp = [0] * (N + 1)

for i in range(N):
    t, p = list(map(int, input().split()))
    T.append(t)
    P.append(p)

for i in range(0, N):
    if T[i] <= N - i:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[N])