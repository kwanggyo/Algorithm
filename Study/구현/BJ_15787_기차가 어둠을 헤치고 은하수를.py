# 2차원 배열 [0, 0, 0, ... 0](20개) X N
# 명령에 따라 집어 넣는다.
# set 안에 str로 연결하여 visited를 체크
# 52252KB, 592ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
train = [['0'] * 20 for _ in range(N)]
ans = set()
for _ in range(M):
    order = list(map(int, input().split()))
    if order[0] == 1:
        train[order[1]-1][order[2]-1] = '1'
    elif order[0] == 2:
        train[order[1]-1][order[2]-1] = '0'
    elif order[0] == 3:
        for k in range(18, -1, -1):
            train[order[1]-1][k+1] = train[order[1]-1][k]
        train[order[1]-1][0] = '0'
    elif order[0] == 4:
        for k in range(1, 20):
            train[order[1]-1][k-1] = train[order[1]-1][k]
        train[order[1]-1][19] = '0'

cnt = 0
while cnt < N:
    ans.add("".join(train[cnt]))
    cnt += 1

print(len(ans))
