# https://www.acmicpc.net/problem/17212
# DP? 점화식 찾기

N = int(input())
coin = [1, 2, 5, 7]
dp = [N] * (N + 1)  # 초기값 : 최대의 개수는 1 * N
dp[0] = 0
for i in range(1, N + 1):
    for c in coin:
        if c <= i and dp[i-c] + 1 < dp[i]:  # 이부분...어떻게 찾지
            dp[i] = dp[i-c] + 1
print(dp[-1])