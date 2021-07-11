# https://www.acmicpc.net/problem/1976
# 플로이드-와샬 활용 Floyd_Warshall
# A-C-B-D로 갈 수 있으면 A-B-C-D로도 갈 수 있다.
# 연습할 겸 거쳐서 가는 최단 거리를 구하고 길이 있으면 가능 여부 반환
# 29200KB 1956ms

N = int(input())
M = int(input())
INF = 0xffffff
city = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
for r in range(N):
    for c in range(N):
        if r == c:      # 이 부분이 없어서 틀렸었음 아마도 1-2-3-3-1 이럴 때 틀리는 듯!
            city[r][c] = 1
        if city[r][c] == 0:
            city[r][c] = INF

for k in range(N):
    for i in range(N):
        for j in range(N):
            if city[i][j] > city[i][k] + city[k][j]:
                city[i][j] = city[i][k] + city[k][j]


for val in order:
    flag = True
    for i in range(len(order)):
        if val - 1 == i:
            continue
        if city[val - 1][order[i] - 1] == INF:
            flag = False
            break
    if flag:
        ans = "YES"
        break
    else:
        ans = "NO"

print(ans)