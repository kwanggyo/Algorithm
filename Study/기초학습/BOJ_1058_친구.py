# https://www.acmicpc.net/problem/1058
# Floyd Warshall
# 29200KB, 92ms

import sys
input = sys.stdin.readline

def Floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j: continue
                if friends[i][j] == 'Y' or (friends[i][k] == 'Y' and friends[k][j] == 'Y'):
                    check[i][j] = 1


N = int(input())
friends = []
for _ in range(N):
    friends.append(list(input()))
check = [[0] * N for _ in range(N)]
ans = 0
Floyd()

for i in range(N):
    cnt = 0
    for j in range(N):
        if check[i][j] == 1:
            cnt += 1
    ans = max(ans, cnt)

print(ans)