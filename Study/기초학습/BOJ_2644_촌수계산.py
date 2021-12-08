# https://www.acmicpc.net/problem/2644

from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    Q = deque()
    Q.append(s)
    check = [0] * (N + 1)
    check[s] = 1
    while Q:
        val = Q.popleft()
        for w in G[val]:
            if check[w] == 0:
                check[w] = 1
                result[w] = result[val] + 1
                Q.append(w)


N = int(input())
num1, num2 = map(int, input().split())
G = [[] for _ in range(N + 1)]
result = [0] * (N + 1)
M = int(input())
for _ in range(M):
    x, y = map(int, input().split())    # x : 부모, y : 자식
    G[x].append(y)
    G[y].append(x)

bfs(num1)   # 각 사람의 부모는 한명이기 때문에
print(result[num2] if result[num2] != 0 else -1)


