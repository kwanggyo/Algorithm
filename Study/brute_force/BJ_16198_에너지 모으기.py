# https://www.acmicpc.net/problem/16198
# insert : https://wikidocs.net/16040
# 30476KB, 140ms
# 여기서 deepcopy를 사용하면 copy보다 3배가 많이 걸렸다 500ms vs 160ms

import sys

input = sys.stdin.readline
N = int(input())
bead = list(map(int, input().split()))
ans = []

def search_energy(idx, energy, arr):
    if idx == 2:
        ans.append(energy)
        return
    else:
        for i in range(1, idx-1):
            tmp = arr.pop(i)
            search_energy(idx - 1, energy + (arr[i-1]*arr[i]), arr)
            arr.insert(i, tmp)

search_energy(N, 0, bead)
print(max(ans))