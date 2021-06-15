# 완전탐색
# 탐색 인덱스를 1부터 시작 n-1까지 r, c 둘다
# 재귀를 통해서 구현한다. 매개변수 활용
# 매개변수 : r, c=, flower_cnt(몇 개 심었는지), cost(비용)
# 방문체크/해제를 해줘야함

def search_flower_cost(r, c, flower_cnt, flower_cost, check):
    global min_cost
    cost = 0
    if flower_cnt == 3:
        if min_cost > flower_cost:
            min_cost = flower_cost
    else:
        for i in range(r, N-1):
            for j in range(c, N-1):
                if check[i][j] == 0 and check[i][j+1] == 0 and check[i+1][j] == 0 and check[i][j-1] == 0 and check[i-1][j] == 0:
                    check[i][j] == 1
                    check[i][j + 1] == 1
                    check[i + 1][j] == 1
                    check[i][j - 1] == 1
                    check[i - 1][j] == 1
                    cost = garden[i][j] + garden[i][j+1] + garden[i+1][j] + garden[i][j-1] + garden[i-1][j]
                    search_flower_cost(i+2, j+2, flower_cnt + 1, flower_cost + cost, check)
                    check[i][j] == 0
                    check[i][j + 1] == 0
                    check[i + 1][j] == 0
                    check[i][j - 1] == 0
                    check[i - 1][j] == 0
                else:
                    search_flower_cost(i + 1, j + 1, flower_cnt, flower_cost, check)




N = int(input())
garden = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * N for _ in range(N)]
min_cost = 987654321
search_flower_cost(1, 1, 0, 0, check)
print(min_cost)