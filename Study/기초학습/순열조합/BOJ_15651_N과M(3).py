# https://www.acmicpc.net/problem/15651
# 중복 조합
# 29452KB, 1948ms
# 29200KB, 1592ms
# 99200KB 248ms

# def comb(idx):
#     if idx == M:
#         print(*ans)
#         return
#     for i in range(N):
#         ans.append(arr[i])
#         comb(idx + 1)
#         ans.pop()
#
#
# N, M = map(int, input().split())
# arr = [i + 1 for i in range(N)]
# ans = []
# comb(0)


# from itertools import product
#
# N, M = map(int, input().split())
# arr = [i + 1 for i in range(N)]
# for i in product(arr, repeat=M):
#     print(' '.join(map(str, i)))


from itertools import product

N, M = map(int, input().split())
arr = list(map(str, range(1, N+1)))
print('\n'.join(list(map(' '.join, product(arr, repeat=M)))))