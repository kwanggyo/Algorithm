# https://www.acmicpc.net/problem/6443
# Backtracking
# 30860KB, 436ms
# 파이썬 내장함수로 구현하면 시간초과가 뜬다..!


import sys

def permutations(idx, N):
    if idx == N:
        print(''.join(ans))
        return
    for i in visited:
        if visited[i]:
            visited[i] -= 1
            ans[idx] = i
            permutations(idx + 1, N)
            visited[i] += 1


N = int(sys.stdin.readline())
for _ in range(N):
    word = sorted(input())
    W = len(word)
    visited = dict()
    for i in range(W):
        if word[i] in visited:
            visited[word[i]] += 1
        else:
            visited[word[i]] = 1
    ans = [0] * W
    permutations(0, W)



#########  50% 시간초과  #########
# from itertools import permutations
# import sys
#
# N = int(sys.stdin.readline())
# for _ in range(N):
#     word = sorted(input())
#     W = len(word)
#     ans = []
#     dupulication_check = set()
#     for i in permutations(word, W):
#         tmp = ''.join(i)
#         if tmp in dupulication_check: continue
#         dupulication_check.add(tmp)
#         print(tmp)
#         # ans.append(tmp)
#     # print('\n'.join(ans))