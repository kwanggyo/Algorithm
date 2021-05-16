# 배열을 2개를 만들어서 기존 배열과 확산 후 배열로 정한다.
# 확산 후 배열에서 방향에 따라 이동시켜준 후 기존 배열에 넣어준다. 후에 cnt + 1
# n초 후에 기존 배열에 들어가있는 수의 총합을 계산
from copy import deepcopy
from collections import deque   # pypy3 161920 KB, 2252ms


def diffusion(Q):
    while Q:
        r, c = Q.popleft()
        move_dust = before_room[r][c] // 5
        total_move_dust = 0
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr == upaircleaner_r and nc == upaircleaner_c:
                continue
            if nr == downaircleaner_r and nc == downaircleaner_c:
                continue
            if 0 <= nr < R and 0 <= nc < C:
                after_room[nr][nc] += move_dust
                total_move_dust += move_dust
        after_room[r][c] -= total_move_dust


# 위쪽 공기청정기 순환
def move_dust_up(r, c):
    after_room[r][c+1] = before_room[r][c]
    after_room[r][c] = 0
    c += 1
    while c < C-1:
        after_room[r][c+1] = before_room[r][c]
        c += 1
    while r > 0:
        after_room[r-1][c] = before_room[r][c]
        r -= 1
    while c > 0:
        after_room[r][c-1] = before_room[r][c]
        c -= 1
    while r < upaircleaner_r - 1:
        after_room[r+1][c] = before_room[r][c]
        r += 1

# 아래쪽 공기청정기 순환
def move_dust_down(r, c):
    after_room[r][c+1] = before_room[r][c]
    after_room[r][c] = 0
    c += 1
    while c < C-1:
        after_room[r][c+1] = before_room[r][c]
        c += 1
    while r < R-1:
        after_room[r+1][c] = before_room[r][c]
        r += 1
    while c > 0:
        after_room[r][c-1] = before_room[r][c]
        c -= 1
    while r > downaircleaner_r + 1:
        after_room[r-1][c] = before_room[r][c]
        r -= 1


R, C, T = map(int, input().split())
before_room = [list(map(int, input().split())) for _ in range(R)]
after_room = deepcopy(before_room)
# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
startQ = deque()
aircleaner = []

# 공기 청정기 위치 찾기
for i in range(R):
    for j in range(C):
        if before_room[i][j] == -1:
            aircleaner.append((i, j))
        else:
            # 계속 쓰기 때문에 하나로 받아둠
            startQ.append((i, j))

# 공기청정기 위치
upaircleaner_r, upaircleaner_c = aircleaner[0]  # 위
downaircleaner_r, downaircleaner_c = aircleaner[1]  # 아래

# 미세먼지 확산
cnt = 0
while cnt < T:  # T 초동안 확산
    tmp = deepcopy(startQ)  # deepcopy를 안하면 Q = [] 으로 됨
    diffusion(tmp)
    before_room = deepcopy(after_room)
    move_dust_up(upaircleaner_r, upaircleaner_c + 1)
    move_dust_down(downaircleaner_r, downaircleaner_c + 1)
    before_room = deepcopy(after_room)
    cnt += 1

total = 2   # 공기청정기 값이 -1, -1 이므로 2를 더해줌
for i in range(R):
    for j in range(C):
        total += after_room[i][j]

print(total)