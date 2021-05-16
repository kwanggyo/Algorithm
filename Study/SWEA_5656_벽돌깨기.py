from collections import deque
from copy import deepcopy

# 안돌아감..

# 벽돌 깨뜨리기
def ping(arr, n):
    global ans
    if n == N:
        block_cnt = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0:  # 벽돌에 적힌 수가 0이 아니면
                    block_cnt += 1  # 카운트
        if ans > block_cnt:
            ans = block_cnt
    else:
        Q = deque()
        copy_array = deepcopy(arr)  # 처음에 들어온 행렬은 바뀌지 않도록
        for c in range(W):
            visited = [[0] * W for _ in range(H)]
            for r in range(H):
                if arr[r][c] != 0:
                    Q.append((r, c))
                    # 벽돌 깨기
                    while Q:
                        r, c = Q.popleft()
                        num = arr[r][c]
                        for i in range(num):
                            dr = [-i, 0, i, 0]
                            dc = [0, i, 0, -i]
                            for k in range(4):
                                nr = r + dr[k]
                                nc = c + dc[k]
                                if 0 <= nr < H and 0 <= nc < W:
                                    if visited[nr][nc] == 0:
                                        visited[nr][nc] = 1
                                        copy_array[nr][nc] = 0
                                        Q.append((nr, nc))

                    # 벽돌 정렬
                    for c in range(W):
                        cnt = H-1
                        for r in range(H-1, -1, -1):
                            if copy_array[r][c] != 0:
                                copy_array[cnt][c] = copy_array[r][c]
                                cnt -= 1

                    ping(deepcopy(copy_array), n + 1)
                    # break  # 줄에서 제일 위에 있는 0이 아닌 벽돌만 깬다.


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(H)]
    Q = deque()
    ans = 180

    ping(block, 0)
    print('#{} {}'.format(tc, ans))
