# https://www.acmicpc.net/problem/2579
# DP
# 30860KB, 84ms
# N이나 N + 1로 리스트를 만들면 런타임 에러 -> 왜 나는지?

N = int(input())
score = [0] * 301
for i in range(N):
    score[i] = int(input())

dp = [0] * 301
dp[0] = score[0]
dp[1] = score[0] + score[1]
# 첫번째 계단을 밟고 오른 경우와 밟지 않고 오른 경우
dp[2] = max(score[0] + score[2], score[1] + score[2])
for i in range(3, N):
    # 마지막 전 계단을 밟은 경우와 밟지 않은 경우
    dp[i] = max(dp[i - 3] + score[i - 1] + score[i], dp[i - 2] + score[i])

print(dp[N - 1])