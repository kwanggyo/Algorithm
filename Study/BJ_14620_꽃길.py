# 완전탐색
# 탐색 인덱스를 1부터 시작 n-1까지 r, c 둘다
# 재귀를 통해서 구현한다. 매개변수 활용
# 매개변수 : r, c, flower_cnt(몇 개 심었는지), cost(비용)
# 방문체크/해제를 해줘야함

def search_flower_cost(r, flower_cnt, flower_cost):
    global min_cost
    if flower_cnt == 3:
        if min_cost > flower_cost:
            min_cost = flower_cost
            return
    else:
        for i in range(r, N-1):
            for j in range(1, N-1):
                if check[i][j] == 0 and check[i][j+1] == 0 and check[i+1][j] == 0 and check[i][j-1] == 0 and check[i-1][j] == 0:
                    check[i][j] = 1
                    check[i][j + 1] = 1
                    check[i + 1][j] = 1
                    check[i][j - 1] = 1
                    check[i - 1][j] = 1
                    cost = garden[i][j] + garden[i][j+1] + garden[i+1][j] + garden[i][j-1] + garden[i-1][j]
                    search_flower_cost(i, flower_cnt + 1, flower_cost + cost)
                    check[i][j] = 0
                    check[i][j + 1] = 0
                    check[i + 1][j] = 0
                    check[i][j - 1] = 0
                    check[i - 1][j] = 0


N = int(input())
garden = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * N for _ in range(N)]
min_cost = 10000
search_flower_cost(1, 0, 0)
print(min_cost)