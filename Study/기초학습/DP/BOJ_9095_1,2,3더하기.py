# https://www.acmicpc.net/problem/9095
# DP
# 30860KB, 72ms
# 점화식 찾기(손으로 써보기)

T = int(input())
dp =[0] * 11
dp[0] = 1
dp[1] = 2
dp[2] = 4
for i in range(3, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(T):
    N = int(input())
    print(dp[N - 1])