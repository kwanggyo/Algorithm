# https://www.acmicpc.net/problem/17352
# 41212KB, 800ms

import sys
input = sys.stdin.readline

def findSet(v):
    if v != p[v]:
        p[v] = findSet(p[v])
    return p[v]

def union(u, v):
    a = findSet(u)
    b = findSet(v)
    if a < b:
        p[b] = a
    else:
        p[a] = b

N = int(input())
p = [i for i in range(N+1)]
for _ in range(N-2):
    a, b = map(int, input().split())
    union(a, b)

ans = '1 '
for k in range(N, 0, -1):
    if k == p[k]:
        ans += str(k)
        break

print(ans)