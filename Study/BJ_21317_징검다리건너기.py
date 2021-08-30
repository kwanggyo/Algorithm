# https://www.acmicpc.net/problem/21317
# dp? // bigbig 점프 어떻게 하지?

import sys
input = sys.stdin.readline

def dfs(idx, bigbig, energy):
    if idx == N:
        ans.append(energy)
        return
    elif idx > N:
        return
    if bigbig == False:
        dfs(idx+3, True, energy + K)
    dfs(idx + 1, bigbig, energy + stones[idx][0])
    dfs(idx + 2, bigbig, energy + stones[idx][1])


N = int(input())
stones = [0] + [list(map(int, input().split())) for _ in range(N-1)]
K = int(input())
ans = []

dfs(1, False, 0)
print(min(ans))