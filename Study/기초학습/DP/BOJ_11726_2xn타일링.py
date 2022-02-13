# https://www.acmicpc.net/problem/11726
# DP
# 30864KB, 72ms
# 손으로 그려보면서 점화식 찾기..?

N = int(input())
dp = [0, 1, 2]
for i in range(3, 1001):
  dp.append(dp[i - 2] + dp[i - 1])
print(dp[N] % 10007)