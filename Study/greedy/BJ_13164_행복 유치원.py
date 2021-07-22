# https://www.acmicpc.net/problem/13164
# 62824KB, 356ms

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
children = list(map(int, input().split()))
dif = []
for i in range(1, N):
    dif.append(children[i] - children[i-1])
dif.sort()
ans = 0
for j in range(N-K):
    ans += dif[j]

print(ans)