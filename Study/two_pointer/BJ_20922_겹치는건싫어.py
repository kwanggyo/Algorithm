import sys
from collections import deque

def search():
    global ans
    Q = deque()
    s, e = 0, 0
    num_dict = {}
    while e < N:
        if arr[e] not in num_dict:
            num_dict[arr[e]] = 1
        else:
            num_dict[arr[e]] += 1
            if num_dict[arr[e]] == M + 1:
                if e - s > ans:
                    ans = e - s
                while Q:
                    val, idx = Q.popleft()
                    num_dict[val] -= 1
                    if val == arr[e]:
                        s = idx + 1
                        break
        Q.append((arr[e], e))
        e += 1
    if ans < len(Q):
        ans = len(Q)


input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
search()
print(ans)