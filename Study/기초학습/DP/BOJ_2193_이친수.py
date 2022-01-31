# https://www.acmicpc.net/problem/2193
# DP
# 30864KB, 68ms
# 1 / 10 / 101, 100 / 1010, 1001, 1000 / 10101, 10100, 10011, 10010, 10000 /
# -> N-1 자리에 0을 추가하는 경오, N-2자리에 01을 추가하는 경우

N = int(input())
dp = [0, 1, 1]
for i in range(3, 91):
    dp.append(dp[i - 2] + dp[i - 1])
print(dp[N])
