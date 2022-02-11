# https://www.acmicpc.net/problem/9663
# Backtracking
# 안되는 경우 -> 1. 같은 열에 다른 퀸, 2. 왼쪽 대각선이나 오른쪽 대각선에 다른 퀸(위에 체스판만 확인하면 됨)
# 해당하는 경우를 식으로 표현
# 3% 이후, 시간초과

def is_possible(x):
    # 이전에 놓았던 퀸 위치를 가져와서 row와 column 차이가 같으면 안됨
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def find_Queen(idx):
    global ans
    if idx == N:
        ans += 1
        # return  # return을 안쓸거면 else를 써줘야한다 !
    else:
        for i in range(N):
            # (x, i)에 퀸을 놓기
            row[idx] = i
            if is_possible(idx):
                find_Queen(idx + 1)


N = int(input())
ans = 0
row = [0] * N
find_Queen(0)
print(ans)
