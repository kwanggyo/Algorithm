# https://www.acmicpc.net/problem/1912
# DP
# 38568KB, 132ms
# append로 만들어보기

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
dp = [0] * N
dp[0] = numbers[0]

for i in range(1, N):
    dp[i] = max(numbers[i], dp[i-1] + numbers[i])

print(max(dp))



# 37% 틀렸습니다.
# N = int(input())
# numbers = list(map(int, input().split()))
# dp = [-1e10] * 100001
# dp[0] = numbers[0]
# dp[1] = numbers[0] if numbers[1] < 0 else numbers[0] + numbers[1]
# for i in range(2, N):
#     if dp[i-1] < 0:
#         dp[i] = numbers[i]
#     else:
#         dp[i] = dp[i-1] + numbers[i]
#
# print(max(dp))