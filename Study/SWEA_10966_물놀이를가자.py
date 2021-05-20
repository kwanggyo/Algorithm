# 모든 L에 대해서 모든 W와의 거리를 구한 후 최솟값을 선택한다.
# 각각의 L의 최솟값을 합친다.

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    summer = [list(input()) for _ in range(N)]
    watter = []
    W_cnt = 0
    for r in range(N):
        for c in range(M):
            if summer[r][c] == 'W':
                watter.append((r, c))

    final_dist = 0
    for i in range(N):
        for j in range(M):
            if summer[i][j] == 'L':
                min_dist = 987654321
                for wat in watter:
                    r, c = wat
                    dist = abs(r-i)
                    if dist > min_dist:
                        break
                    dist += abs(c-j)

                    if dist == 1:
                        min_dist = dist
                        break

                    if min_dist > dist:
                        min_dist = dist
                final_dist += min_dist

    print('#{} {}'.format(tc, final_dist))
