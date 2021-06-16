# 그래프 탐색
# 함수를 여러개 만들어서 배치
# 현재 폭탄을 가지고 있는 곳을 저장하는 함수
# 비어있는 곳에 폭탄을 설치하는 함수
# 폭탄을 터트리는 함수

def search_bumb(map):
    for r in range(R):
        for c in range(C):
            if map[r][c] == 'O':
                bumb_li.append((r, c))

def make_bumb(map):
    for r in range(R):
        for c in range(C):
            map[r][c] = 'O'

def bumbbumb(bumb_li, map):
    r, c = bumb_li.pop()
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

R, C, N = map(int, input().split())
bumb_map = [list(input()) for _ in range(R)]
bumb_li = []
# 우 하 상 좌
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

cnt = 0
while cnt < N:
    pass