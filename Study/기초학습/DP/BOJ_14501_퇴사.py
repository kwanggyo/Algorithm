# https://www.acmicpc.net/problem/14501
# DP

import sys
input = sys.stdin.readline

dp = [0] * 16
N = int(input())
P = [0] * N
for _ in range(N):
    t, p = map(int, input().split())
    P[t] = p

