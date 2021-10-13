# 0: 빈칸, 1: 집, 2: 치킨집
# r, c가 1부터 시작 !
# M 개의 치킨집을 가져오는 경우의 수를 구하고
# 각 경우의 수에 대한 도시의 치킨 거리값 저장 후 최솟값 출력

def search(idx, start):     # 28776 // 524ms
    global ans
    if idx == M:
        city_dist = 0
        for i in range(N):
            for j in range(N):
                if area[i][j] == 1:
                    chick_dist = 100
                    for ch in res:  # 조합으로 계산한 경우의 수가 res에 담겨 있다
                        r, c = ch   # 여기서 하나씩 빼면서
                        dist = abs(r - i) + abs(c - j)  # 치킨거리 계산
                        if chick_dist > dist:   # 최소 치킨 거리 찾는 부분
                            chick_dist = dist
                    city_dist += chick_dist # 최소 치킨 거리를 찾아서 도시의 치킨거리에 더해준다.
                    if city_dist >= ans:    # 가지치기 부분 // 도시의 치킨거리를 계산하는데 이전에 구했던 최소 도시의 치킨거리보다 커지만 더이상 계산 x
                        return
        if ans > city_dist: # 최소 도시의 치킨거리 비교 부분
            ans = city_dist
    else:
        for k in range(start, chick_cnt):   # 조합을 구하는 부분 nCr에서 chick_cnt가 n부분이다.
            res.append(chicken[k])
            search(idx+1, k+1)
            res.pop()


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
chicken = []    # 치킨 집의 좌표를 담을 곳
chick_cnt = 0   # 조합에서의 N값 (ex. N 개중에 M개를 뽑을 거임)
city_dist = 0   # 도시의 치킨 거리
ans = 987654321 # 최종 답
res = []


for i in range(N):
    for j in range(N):
        if area[i][j] == 2:
            chicken.append((i, j))  # chick_cnt에서 M개 선택하는 조합을 구할거임
            chick_cnt += 1

search(0, 0)
print(ans)