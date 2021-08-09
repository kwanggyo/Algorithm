# https://www.acmicpc.net/problem/17829
# 74976KB, 964ms

import copy

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
while N > 1:
    result = [[0] * (N//2) for _ in range(N//2)]
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            values = [arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]]
            values.sort(reverse=True)
            result[i//2][j//2] = values[1]
    N //= 2
    arr = copy.deepcopy(result)

print(arr[0][0])
