# https://www.acmicpc.net/problem/16926
# 구현
# PyPy3 126260KB, 824ms
# Python -> 시간초과

import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
NM = min(N, M) // 2

while cnt < R:
    for i in range(NM):
        s_x, s_y = i, i
        s_value = arr[s_x][s_y]

        # 바뀌기 전 값을 저장해 둔다.
        for j in range(i + 1, N - i):  # ↓
            s_x = j
            prev_value = arr[s_x][s_y]
            arr[s_x][s_y] = s_value
            s_value = prev_value

        for j in range(i + 1, M - i):  # →
            s_y = j
            prev_value = arr[s_x][s_y]
            arr[s_x][s_y] = s_value
            s_value = prev_value

        for j in range(i + 1, N - i):  # ↑
            s_x = N - j - 1
            prev_value = arr[s_x][s_y]
            arr[s_x][s_y] = s_value
            s_value = prev_value

        for j in range(i + 1, M - i):  # ←
            s_y = M - j - 1
            prev_value = arr[s_x][s_y]
            arr[s_x][s_y] = s_value
            s_value = prev_value
    cnt += 1

for i in range(N):
    print(' '.join(map(str, arr[i])))
