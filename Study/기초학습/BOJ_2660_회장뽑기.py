# https://www.acmicpc.net/problem/2660
# 29200KB, 84ms

N = int(input())
INF = 0xffff
dist = [[INF] * (N+1) for _ in range(N+1)]
while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    dist[a][b] = 1
    dist[b][a] = 1

for i in range(1, N+1):
    dist[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][j] == 1 or dist[i][j] == 0:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

point = []
for i in range(1, N+1):
    point.append(max(dist[i][1:]))

min_point = min(point)
print(min_point, point.count(min_point))
for idx, val in enumerate(point):
    if val == min_point:
        print(idx+1, end=' ')



# 안되는 코드
# while True:
#     a, b = map(int, input().split())
#     if a == -1:
#         break
#     graph[a-1][b-1] = 1
#     graph[b-1][a-1] = 1
#
# point_list = [0] * N
# for i in range(N):
#     point_list[i] = N - sum(graph[i])
#
# point = N
# for j in range(N):
#     if point_list[j] < point:
#         point_member = [j+1]
#         point = point_list[j]
#     elif point_list[j] == point:
#         point_member.append(j+1)
#
# print(str(point) + ' ' + str(len(point_member)))
# print(*point_member)



