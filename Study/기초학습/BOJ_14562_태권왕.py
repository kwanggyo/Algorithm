# https://www.acmicpc.net/problem/14562
# search : 29200KB, 212ms
# search2 : 32748KB, 100ms

# 2가지 경우의 수로 재귀를 돌린다.

# def search(s, t, cnt):
#     if s == t:
#         ans.append(cnt)
#     elif s > t:
#         return
#     search(s*2, t+3, cnt+1)
#     search(s+1, t, cnt+1)


from collections import deque

def search2(S, T):
    Q = deque()
    Q.append((S, T, 0))
    while Q:
        s, t, cnt = Q.popleft()
        if s == t:
            return cnt
        elif s < t:
            Q.append((s*2, t+3, cnt + 1))
            Q.append((s+1, t, cnt + 1))


C = int(input())
for tc in range(1, C+1):
    S, T = map(int, input().split())
    # ans = []
    # search(S, T, 0)
    # print(min(ans))
    print(search2(S, T))

