# https://www.acmicpc.net/problem/12761
# BFS

# 갈 수 있는 방법 : +1, -1, +A, -A, +B, -B, Ax, Bx

import sys
input = sys.stdin.readline


def bfs(pos, cnt):
    global ans
    if ans < cnt:
        return
    if N == M:
        ans = cnt
        return

A, B, N, M = map(int, input().split())
ans = 0