# https://www.acmicpc.net/problem/15663
# 33044KB, 224ms

import sys
input = sys.stdin.readline

def perm(idx):
    if idx == M:
        tmp = ' '.join(map(str, res))
        if tmp not in result:       # in list가 아니라 in set 이어야 시간초과를 통과할 수 있다!!
            result.add(tmp)
            print(tmp)
    else:
        for i in range(N):
            if check[i] == 0:
                check[i] = 1
                res.append(arr[i])
                perm(idx + 1)
                check[i] = 0
                res.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
check = [0] * N
res = []
result = set()

perm(0)

