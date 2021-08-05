# https://www.acmicpc.net/problem/11265
# PyPy 127892KB	 1100ms
# Python 32012KB  7328ms
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
party = [list(map(int, input().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if party[i][j] > party[i][k] + party[k][j]:
                party[i][j] = party[i][k] + party[k][j]
for _ in range(M):
    A, B, C = map(int, input().split())
    if party[A-1][B-1] <= C:
        print("Enjoy other party")
    else:
        print("Stay here")

# ans = ''
# for _ in range(M):
#     A, B, C = map(int, input().split())
#     if party[A-1][B-1] <= C:
#         ans += "Enjoy other party"
#     else:
#         ans += "Stay here"
#     ans += "\n"
# print(ans)