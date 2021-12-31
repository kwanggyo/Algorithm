# https://www.acmicpc.net/problem/15654
# 순열
# 29200KB, 236ms
# 29200KB, 156ms


import sys
input = sys.stdin.readline

def perm(idx):
    if idx == M:
        print(*ans)
        return
    for i in range(N):
        if visited[i] == 1: continue
        ans.append(arr[i])
        visited[i] = 1
        perm(idx + 1)
        visited[i] = 0
        ans.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * N
arr.sort()
ans = []
perm(0)


# from itertools import permutations
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# for i in permutations(arr, M):
#     print(' '.join(map(str, i)))