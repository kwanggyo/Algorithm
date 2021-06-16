# 그래프 탐색
# 함수를 여러개 만들어서 배치
# 현재 폭탄을 가지고 있는 곳을 저장하는 함수
# 비어있는 곳에 폭탄을 설치하는 함수
# 폭탄을 터트리는 함수

# 31756KB, 3416ms
def search_bumb(map):   # 폭탄 찾기
    for r in range(R):
        for c in range(C):
            if map[r][c] == 'O':
                bumb_li.append((r, c))


def make_bumb(map):     # 폭탄 만들기
    for r in range(R):
        for c in range(C):
            map[r][c] = 'O'


def bumbbumb(bumb_li, map):     # 폭탄 터트리기
    while bumb_li:
        r, c = bumb_li.pop()
        map[r][c] = '.'
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                map[nr][nc] = '.'


R, C, N = map(int, input().split())
bumb_map = [list(input()) for _ in range(R)]
bumb_li = []
# 우 하 상 좌
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

cnt = 1
while True:
    if cnt >= N:
        break
    search_bumb(bumb_map)
    make_bumb(bumb_map)
    cnt += 1
    if cnt >= N:
        break
    bumbbumb(bumb_li, bumb_map)
    cnt += 1
    if cnt >= N:
        break

result = ''
for i in range(R):
    result = ''.join(bumb_map[i])
    print(result)