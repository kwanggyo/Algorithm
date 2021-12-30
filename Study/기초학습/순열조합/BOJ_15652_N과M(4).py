# https://www.acmicpc.net/problem/15652
# 중복 조합
# 29452KB, 80ms
# 29200KB, 76ms


# def comb(idx, start):
#     if idx == M:
#         print(*ans)
#         return
#     for i in range(start, N):
#         ans.append(arr[i])
#         comb(idx + 1, i)
#         ans.pop()
#
# N, M = map(int, input().split())
# arr = [i + 1 for i in range(N)]
# ans = []
# comb(0, 0)


from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = [i + 1 for i in range(N)]
for i in combinations_with_replacement(arr, M):
    print(' '.join(map(str, i)))