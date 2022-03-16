# https://www.acmicpc.net/problem/1463
# DP
# 38672KB, 672ms
# 10을 구하려면 9를 통해 구하고 9를 구하려면 3을 통해, 3은 1을 통해 구해진다

N = int(input())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i-1] + 1 # 2와 3으로 나누어 떨어지지 않는다면 무조건 1을 빼야했기 때문에

    # 나누어 떨어지는게 이득
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])