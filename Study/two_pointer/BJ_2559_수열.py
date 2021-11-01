# https://www.acmicpc.net/problem/2559
# 38188KB, 120ms

N, K = map(int, input().split())
temperature = list(map(int, input().split()))
result = -0xffffffff
temp_sum = 0
for k in range(K):
    temp_sum += temperature[k]
result = temp_sum

for i in range(N-K):
    s, e = i, i + K
    temp_sum = temp_sum - temperature[s] + temperature[e]
    if result < temp_sum:
        result = temp_sum

print(result)


# 시간초과
# for i in range(0, N-K):
#     temp_sum = 0
#     for j in range(i, i + K):
#         temp_sum += temperature[j]
#     if result < temp_sum:
#         result = temp_sum
#
# print(result)
