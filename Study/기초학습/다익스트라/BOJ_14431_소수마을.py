# https://www.acmicpc.net/problem/14431
# Dijkstra
# 다익스트라 + 소수 판별 함수 + 좌표 사이 거리 계산 함수

# 시작점에서 갈 수 있는지 구한다.
from heapq import heappush, heappop
from collections import deque
import sys
input = sys.stdin.readline

# 두점 사이의 거리를 구하는 함수
def dist_cal(x1, y1, x2, y2):
    print((x1-x2)**2, (y1-y2)**2)
    value = int(((x1-x2)**2 + (y1-y2)**2)**0.5)
    return value

# 소수 판별 함수
def isPrimeNumber(x):
    if x < 2: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

# 최단거리(다익스트라)
def BFS(x, y):
    HQ = []
    heappush(HQ, (0, x, y))
    dist = [INF] * (N + 1)
    while HQ:
        dist, r, c = heappop(HQ)
        if r == er and c == ec:
            return dist
        for new_r, new_c in village:
            new_dist = dist_cal(r, c, new_r, new_c)
            print('new_dist', new_dist)
            if isPrimeNumber(new_dist):
                if 
                heappush(HQ, (dist + new_dist, new_r, new_c))
    return -1

sr, sc, er, ec = map(int, input().split())
N = int(input())
village = []
INF = 1e9
for _ in range(N):
    a, b = map(int, input().split())
    village.append(((a, b)))

print(BFS(sr, sc))
