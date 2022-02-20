# https://programmers.co.kr/learn/courses/30/lessons/42898
# DP

# 갈 수 있으면 1 못가면 0
# 자신의 위와 왼쪽의 값을 합친 것이 경우의 수

def solution(m, n, puddles):
    route = [[0] * m for _ in range(n)]
    route[0][0] = 1
    # 인덱스 맞춰서 못가는 부분 체크
    for c, r in puddles:    # 좌표값이 거꾸로 주어지는 것 주의!
        route[r-1][c-1] = 0
    # 위와 왼쪽 값을 더해서 갈 수 있는 경우의 수 저장
    for i in range(0, n):
        for j in range(0, m):
            if route[i][j] == 0: continue
            route[i][j] = (route[i-1][j] + route[i][j-1]) %1000000007

    answer = route[n-1][m-1]
    return answer



print(solution(4, 3, [[2, 2]]))