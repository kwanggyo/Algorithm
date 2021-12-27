# https://www.acmicpc.net/problem/15649
# 순열
# 29452KB 236ms
# 29200KB, 144ms -> itertools 사용이 더 빠르다.

# def perm(idx):
#     if idx == M + 1:
#         print(*ans)
#         return
#     for i in range(1, N + 1):
#         if visited[i] == 0:
#             visited[i] = 1
#             ans.append(i)
#             perm(idx + 1)
#             visited[i] = 0
#             ans.pop()
#
#
# N, M = map(int, input().split())
# arr = [i for i in range(1, N + 1)]
# ans = []
# visited = [0] * (N + 1)
# perm(1)


from itertools import permutations


N, M = map(int, input().split())
arr = [i + 1 for i in range(N)]
for i in permutations(arr, M):  # tuple 형태로 나옴 / ex. (1, 2)
    print(' '.join(map(str, i)))

