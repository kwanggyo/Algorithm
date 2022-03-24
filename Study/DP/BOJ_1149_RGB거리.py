# https://www.acmicpc.net/problem/1149
# DP
# 30864KB, 108ms

N = int(input())
color = [list(map(int, input().split())) for _ in range(N)]
dp = []

for i in range(1, N):
    # 0, 1, 2 = 빨, 초, 파
    color[i][0] = min(color[i - 1][1], color[i - 1][2]) + color[i][0]
    color[i][1] = min(color[i - 1][0], color[i - 1][2]) + color[i][1]
    color[i][2] = min(color[i - 1][0], color[i - 1][1]) + color[i][2]
print(min(color[N - 1][0], color[N - 1][1], color[N - 1][2]))
