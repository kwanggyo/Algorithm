# https://www.acmicpc.net/problem/14501
# DP
# 30864KB, 68ms

import sys
input = sys.stdin.readline

dp = [0] * 16
N = int(input())
T = [0] * N
P = [0] * N
for k in range(N):
    t, p = map(int, input().split())
    T[k] = t
    P[k] = p

for i in range(N - 1, -1, -1):
    if T[i] + i > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])

print(dp[0])