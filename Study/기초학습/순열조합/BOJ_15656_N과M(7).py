# https://www.acmicpc.net/problem/15657
# 30864KB, 76ms
# 중복 조합

from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in combinations_with_replacement(arr, M):
    print(' '.join(map(str, i)))
