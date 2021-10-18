# https://www.acmicpc.net/problem/1106
# 1. N이 큰 순서대로 정렬 후
# 2. 첫번째 인덱스 값으로 목표 N을 나눈 후 몫부터 1씩 내려오며 가능한 조합을 구한다.
# 3. 그 조합의 비용을 구하여 비교한다.


import sys
input = sys.stdin.readline
C, N = map(int, input().split())
hotel = []
INF = 0xfffff
dp = [INF] * (C*100 + 1)
dp[0] = 0

for i in range(N):
    c, n = map(int, input().split())
    print(c, n)
    for j in range(C*100):
        if dp[j] == INF: continue
        for k in range(1, C*100):
            if j+k*n > C*100 + 1: break
            dp[j+k*n] = min(dp[j+k*n], dp[j]+k*c)

print(len(dp))
print(dp)



# import sys
# input = sys.stdin.readline
# C, N = map(int, input().split())
# hotel = []
# ans = []
#
# for _ in range(N):
#     c, n = map(int, input().split())
#     hotel.append((c, n))
# hotel.sort(key=lambda x : x[1], reverse=True)
# # hotel2 = sorted(hotel, key=lambda x:x[1], reverse=True)
# div = C // hotel[0][1]
# remainder = C - div * hotel[0][0]
# cost = div * hotel[0][0]
#
# def combination(div, remainder, cost):
#     if remainder == 0:
#         ans.append(cost)
#         return
#     if remainder < 0:
#         return
#     for i in range(1, N):
#         # 잘못된 풀이 -> DP로 해야한다

