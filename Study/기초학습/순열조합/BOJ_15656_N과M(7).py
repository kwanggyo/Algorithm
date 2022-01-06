# https://www.acmicpc.net/problem/15656
# 중복 조합
# 30864KB, 1604ms
# 137648KB, 280ms

# from itertools import product
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# for i in product(arr, repeat=M):
#     print(' '.join(map(str, i)))

from itertools import product
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print("\n".join(map(' '.join, product(map(str, arr), repeat=M))))
