# https://www.acmicpc.net/problem/15655
# 조합
# 29200KB, 68ms

from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in combinations(arr, M):
    print(' '.join(map(str, i)))