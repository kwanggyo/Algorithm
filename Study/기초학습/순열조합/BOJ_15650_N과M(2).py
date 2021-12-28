# https://www.acmicpc.net/problem/15650
# 조합
# 29200KB, 64ms
# 29200KB, 68ms


# def comb(idx, start):
#     if idx == M:
#         print(*ans)
#         return
#     for i in range(start, N):
#             ans.append(arr[i])
#             comb(idx + 1, i + 1)
#             ans.pop()
#
#
# N, M = map(int, input().split())
# arr = [i + 1 for i in range(N)]
# ans = []
# comb(0, 0)


from itertools import combinations, combinations_with_replacement

N, M = map(int, input().split())
arr = [i + 1 for i in range(N)]
for i in combinations(arr, M):
    print(' '.join(map(str, i)))


