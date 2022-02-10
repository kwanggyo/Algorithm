# https://www.acmicpc.net/problem/9663
# Backtracking

def find_Queen(idx, r, c, arr):
    global ans
    if idx == N:
        ans += 1
        return
    for i in range(N):
        nr = r + 1
        nc = c + i
        for pick_r, pick_c in arr:
            if pick_c - 1 == nc or pick_c + 1 == nc:
                continue
            arr.append((nr, nc))
            find_Queen(idx + 1, nr, nc, arr)
            arr.pop()
    return




N = int(input())
ans = 0
find_Queen(0, 0, 0, [(0, 0)])
print(ans)
