# https://www.acmicpc.net/problem/15270
# 제일 큰 DFS 깊이?
# 틀림 -> 답 찾아봄
# 29200KB 196ms

def dfs(curr, cnt):
    global ans

    if ans < cnt:
        ans = cnt

    if curr == N:   # 위의 if문과 순서가 바뀌면 안된다. cnt 값이 바뀌고 종료 조건을 비교해야한다.
        return

    if visit[curr] == 0:
        for i in range(curr + 1, N + 1):
            if visit[i] == 0 and i in G[curr]:  # 방문하지 않았고 현재 사람(curr)의 친구이면
                visit[curr] = 1 # 현재 사람과
                visit[i] = 1    # 현재 사람의 친구를 방문(연결)
                dfs(curr + 1, cnt + 2)  # 2명이 연결되었으니 cnt + 2
                visit[curr] = 0
                visit[i] = 0
    dfs(curr + 1, cnt)  # 해당하는 친구를 연결하지 않고 지나간다, 친구가 없을 경우에도 계속 진행하기 위해


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

ans = 0
visit = [0] * (N + 1)
dfs(1, 0)

if N > ans:
    print(ans + 1)
else:
    print(ans)

# def dfs(v):
#     check[v] = 1
#     res.append(v)
#     for w in G[v]:
#         if check[w] == 0:
#             dfs(w)
#
#
# N, M = map(int, input().split())
# G = [[] for _ in range(N+1)]
# for _ in range(M):
#     u, v = map(int, input().split())
#     G[u].append(v)
#     G[v].append(u)
#
# ans = []
# for i in range(1, N+1):
#     res = []
#     check = [0] * (N+1)
#     dfs(i)
#     ans.append(len(res))
#
# result = max(ans)
# if N > result and result % 2 == 0:
#     print(result + 1)
# else:
#     print(result)

