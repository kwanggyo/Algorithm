# https://www.acmicpc.net/problem/15663
# 순열, 중복제거
# 36532KB, 112ms

from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
same = set()
ans = []
for i in permutations(arr, M):
    if i in same: continue
    ans.append(' '.join(map(str, i)))
    same.add(i)
print('\n'.join(ans))