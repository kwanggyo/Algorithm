# https://www.acmicpc.net/problem/2212
# 30220KB, 96ms

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()
dif = []
ans = 0
for i in range(1, N):
    dif.append(arr[i] - arr[i-1])
dif.sort()
for j in range(N-K):    # K값이 더 크면 for문 안돌아감 -> 0 출력
    ans += dif[j]
print(ans)