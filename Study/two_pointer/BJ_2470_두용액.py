# 40620KB, 152ms

import sys
input = sys.stdin.readline
N = int(input())
solution = list(map(int, input().split()))
solution.sort()
s, e = 0, N-1
ans_li = [solution[s], solution[e]]
min_val = solution[s] + solution[e]
while s < e:
    val = solution[s] + solution[e]
    if abs(val) < abs(min_val):
        min_val = val
        ans_li[0] = solution[s]
        ans_li[1] = solution[e]
        if min_val == 0:
            break
    if val < 0:
        s += 1
    else:
        e -= 1
print(*ans_li)

# N = int(input()) -> 시간초과
# solution = list(map(int, input().split()))
# ans_li = [0, 0]
# min_val = 1000000000
# for i in range(N):
#     for j in range(i+1, N):
#         if abs(solution[i]+solution[j]) < min_val:
#             min_val = abs(solution[i]+solution[j])
#             ans_li[0] = solution[i]
#             ans_li[1] = solution[j]
# print(*ans_li)


# 정렬한 후 비교 -> 이상함
# i 값이 -이면 +값으로 가서 비교
# def search(s, e):
#     while s < e:
#         c = (s + e) // 2
#         if solution[c] < 0:
#             s = c + 1
#         else:
#             e = c
#     return s
#
#
# N = int(input())
# solution = list(map(int, input().split()))
# ans_li = [0, 0]
# solution.sort()
# mid = search(0, N-1)
# start = 0
# if mid == N - 1:
#     ans_li[0] = mid - 1
#     ans_li[1] = mid
# elif mid == 0:
#     ans_li[0] = start
#     ans_li[1] = start + 1
# else:
#     min_val = solution[start] - solution[mid]
#     mid += 1
#     while start < mid and mid < N-1:
#         if solution[start] + solution[mid] == 0:
#             ans_li[0] = solution[start]
#             ans_li[1] = solution[mid]
#             break
#         elif (solution[start] + solution[mid]) < min_val:
#             min_val = solution[start] + solution[mid]
#             ans_li[0] = solution[start]
#             ans_li[1] = solution[mid]
#             mid += 1
#         elif (solution[start] + solution[mid]) >= min_val:
#             start += 1
# print(*ans_li)
