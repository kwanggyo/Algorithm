# 공이 어디서 오냐에 따라 벽에 부딪쳤을때 바뀌는 방향이 달라짐
# 하 : 아래 방향으로 감, 상 : 위 방향으로 감 ... -> 기준
# 1 : 하 -> 오, 왼 -> 상
# 2 : 상 -> 오, 왼 -> 하
# 3 : 상 -> 왼, 오 -> 하
# 4 : 하 -> 왼, 오 -> 상
# 5 : 상 -> 하, 하 -> 상, 왼 -> 오, 오 -> 왼
# 바운드리 벽을 만날 때에도 반대로 온다.
# 6 ~ 10 : 웜홀
# -1 블랙홀
# 처음 핀볼이 상, 하, 좌, 우 4가지 방향으로 진행할 수 있음 -> 4가지 길을 조사하면 된다 ! 0인 부분에서 시작 가능
# 웜홀에 빠지면 동일한 숫자의 웜홀로 나오게 된다. 진행 방향은 유지 ! -> 진행 방향을 항상 변수로 가지고 있어야함
# --------------------- #
# 현재 진행하는 방향을 가지고 있어야 한다.
# 핀볼의 시작 위치를 가지고 있어야 한다.
# 벽에 부딪칠때마다 카운트를 해야한다.
# 웜홀에 들어갔을 때 반대의 웜홀 좌표를 알아야 한다. -> 미리 리스트에 튜플로 저장해둔다. 웜홀에 들어갔을 때 인덱스로 비교
# -> 무한 루프..
from collections import deque

def movePinball(Q, first_r, first_c):
    finish_cnt = 0
    cnt = 0
    while Q:
        r, c, direction = Q.popleft()
        if r == first_r and c == first_c:
            finish_cnt += 1
            if finish_cnt == 2:
                return cnt
        if direction == 0:  # 위쪽 방향
            if r - 1 < 0:
                cnt += 1
                Q.append((r, c, 2))
                continue
            r -= 1
            while pinball_map[r][c] == 0:
                r -= 1
            if pinball_map[r][c] == -1:
                return cnt
            elif pinball_map[r][c] == 1:    # 상 -> 하
                return 2*cnt + 1
            elif pinball_map[r][c] == 2:    # 상 -> 오
                cnt += 1
                Q.append((r, c+1, 1))
            elif pinball_map[r][c] == 3:    # 상 -> 왼
                cnt += 1
                Q.append((r, c-1, 3))
            elif pinball_map[r][c] == 4:    # 상 -> 하
                return 2 * cnt + 1
            elif pinball_map[r][c] == 5:    # 상 -> 하
                return 2 * cnt + 1
            elif pinball_map[r][c] >= 6:
                if wormhole[pinball_map[r][c] - 6][0][0] == r and wormhole[pinball_map[r][c] - 6][0][1] == c:
                    r, c = wormhole[pinball_map[r][c] - 6][1][0], wormhole[pinball_map[r][c] - 6][1][1]
                else:
                    r, c = wormhole[pinball_map[r][c] - 6][0][0], wormhole[pinball_map[r][c] - 6][0][1]
                Q.append((r, c, 0))

        elif direction == 1:  # 오른쪽 방향
            if c + 1 > N:
                cnt += 1
                Q.append((r, c, 3))
                continue
            c += 1
            while pinball_map[r][c] == 0:
                c += 1
            if pinball_map[r][c] == -1:
                return cnt
            elif pinball_map[r][c] == 1:    # 오 -> 왼
                return 2*cnt + 1
            elif pinball_map[r][c] == 2:    # 오 -> 왼
                return 2 * cnt + 1
            elif pinball_map[r][c] == 3:    # 오 -> 하
                cnt += 1
                Q.append((r+1, c, 2))
            elif pinball_map[r][c] == 4:    # 오 -> 상
                cnt += 1
                Q.append((r-1, c, 0))
            elif pinball_map[r][c] == 5:    # 오 -> 왼
                return 2 * cnt + 1
            elif pinball_map[r][c] >= 6:
                if wormhole[pinball_map[r][c] - 6][0][0] == r and wormhole[pinball_map[r][c] - 6][0][1] == c:
                    r, c = wormhole[pinball_map[r][c] - 6][1][0], wormhole[pinball_map[r][c] - 6][1][1]
                else:
                    r, c = wormhole[pinball_map[r][c] - 6][0][0], wormhole[pinball_map[r][c] - 6][0][1]
                Q.append((r, c, 1))

        elif direction == 2:  # 아래쪽 방향
            if r + 1 > N:
                cnt += 1
                Q.append((r, c, 2))
                continue
            r -= 1
            while pinball_map[r][c] == 0:
                r += 1
            if pinball_map[r][c] == -1:
                return cnt
            elif pinball_map[r][c] == 1:    # 하 -> 오
                cnt += 1
                Q.append((r, c+1, 1))
            elif pinball_map[r][c] == 2:    # 하 -> 상
                return 2*cnt + 1
            elif pinball_map[r][c] == 3:    # 하 -> 상
                return 2 * cnt + 1
            elif pinball_map[r][c] == 4:    # 하 -> 왼
                cnt += 1
                Q.append((r, c-1, 3))
            elif pinball_map[r][c] == 5:    # 하 -> 상
                return 2 * cnt + 1
            elif pinball_map[r][c] >= 6:
                if wormhole[pinball_map[r][c] - 6][0][0] == r and wormhole[pinball_map[r][c] - 6][0][1] == c:
                    r, c = wormhole[pinball_map[r][c] - 6][1][0], wormhole[pinball_map[r][c] - 6][1][1]
                else:
                    r, c = wormhole[pinball_map[r][c] - 6][0][0], wormhole[pinball_map[r][c] - 6][0][1]
                Q.append((r, c, 2))

        elif direction == 0:  # 위쪽 방향
            if c - 1 < 0:
                cnt += 1
                Q.append((r, c, 2))
                continue
            c -= 1
            while pinball_map[r][c] == 0:
                r -= 1
            if pinball_map[r][c] == -1:
                return cnt
            elif pinball_map[r][c] == 1:    # 왼 -> 상
                cnt += 1
                Q.append((r-1, c, 0))
            elif pinball_map[r][c] == 2:    # 왼 -> 하
                cnt += 1
                Q.append((r+1, c, 2))
            elif pinball_map[r][c] == 3:    # 왼 -> 오
                return 2 * cnt + 1
            elif pinball_map[r][c] == 4:    # 왼 -> 오
                return 2 * cnt + 1
            elif pinball_map[r][c] == 5:    # 왼 -> 오
                return 2 * cnt + 1
            elif pinball_map[r][c] >= 6:
                if wormhole[pinball_map[r][c] - 6][0][0] == r and wormhole[pinball_map[r][c] - 6][0][1] == c:
                    r, c = wormhole[pinball_map[r][c] - 6][1][0], wormhole[pinball_map[r][c] - 6][1][1]
                else:
                    r, c = wormhole[pinball_map[r][c] - 6][0][0], wormhole[pinball_map[r][c] - 6][0][1]
                Q.append((r, c, 3))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pinball_map = [list(map(int, input().split())) for _ in range(N)]
    wormhole = [[] for _ in range(5)]       # 웜홀을 리스트에 저장해놓기 위해
    cnt_li = []
    Q = deque()
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if pinball_map[i][j] >= 6:
                wormhole[pinball_map[i][j] - 6].append((i, j))
    for r in range(N):
        for c in range(N):
            if pinball_map[r][c] == 0:
                Q.append((r, c, 0))
                cnt_li.append(movePinball(Q, r, c))
                Q.append((r, c, 1))
                cnt_li.append(movePinball(Q, r, c))
                Q.append((r, c, 2))
                cnt_li.append(movePinball(Q, r, c))
                Q.append((r, c, 3))
                cnt_li.append(movePinball(Q, r, c))

    print('#{} {}'.format(tc, max(cnt_li)))
