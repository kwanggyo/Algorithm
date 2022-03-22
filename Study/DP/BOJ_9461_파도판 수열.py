# https://www.acmicpc.net/problem/9461
# DP
# 30864KB, 80ms

triangle = [0 for i in range(101)]
triangle[1] = 1
triangle[2] = 1
triangle[3] = 1
for i in range(0, 98):
    triangle[i + 3] = triangle[i] + triangle[i + 1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(triangle[N])