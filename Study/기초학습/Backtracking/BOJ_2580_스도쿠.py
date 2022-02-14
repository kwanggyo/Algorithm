# https://www.acmicpc.net/problem/2580
# Backtracking
# python : 시간초과, pypy3 : 155444KB, 3276ms   3x3(1)
# python : 시간초과, pypy3 : 159332KB, 3888ms   3x3(2)

# 가로, 세로, 3x3 비교

import sys
input = sys.stdin.readline

# 가로
def check_row(r, x):
    for i in range(9):
        if x == arr[r][i]:
            return False
    return True

# 세로
def check_column(c, x):
    for i in range(9):
        if x == arr[i][c]:
            return False
    return True

# 3x3(1)
# def check_square(r, c, x):
#     nr = (r // 3) * 3
#     nc = (c // 3) * 3
#     for i in range(3):
#         for j in range(3):
#             if x == arr[nr + i][nc + j]:
#                 return False
#     return True

# 3x3(2)
def check_square(r, c, x):
    r = (r // 3) * 3
    c = (c // 3) * 3
    for i in range(r, r + 3):  # r, r + 3
        for j in range(c, c + 3):  # c, c + 3
            if x == arr[i][j]:    # i, j로 하면 안된다..!
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*arr[i])
        exit(0)

    for i in range(1, 10):
        r = blank[idx][0]
        c = blank[idx][1]
        # 조건을 전부 만족하는지 확인
        if check_row(r, i) and check_column(c, i) and check_square(r, c, i):
            arr[r][c] = i
            dfs(idx + 1)
            arr[r][c] = 0


arr = [[] for _ in range(9)]
for i in range(9):
    arr[i] = list(map(int, input().split()))
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i, j))

dfs(0)



# ### 테케는 맞지만 바로 틀렸습니다 코드 -> 공통으로 들어갈 수 있는게 2개이면 어떻게 할 것인지?
# ### 0을 전부 넣어서 돌리면 안됨
# import sys
# input = sys.stdin.readline
#
# arr = [[] for _ in range(9)]
# for i in range(9):
#     arr[i] = list(map(int, input().split()))
#
# def check_row(r):
#     visited_row = [0] * 10
#     ans_list = []
#     # 해당 행에서 없는 숫자를 확인한다.
#     for i in range(9):
#         if arr[r][i] != 0:
#             visited_row[arr[r][i]] = 1
#     # 없는 숫자들을 담은 리스트를 반환한다.
#     for j in range(1, 10):
#         if visited_row[j] == 0:
#             ans_list.append(j)
#     return ans_list
#
#
# def check_column(c):
#     visited_column = [0] * 10
#     ans_list = []
#     # 해당 열에서 없는 숫자를 확인한다.
#     for i in range(9):
#         if arr[i][c] != 0:
#             visited_column[arr[i][c]] = 1
#     # 없는 숫자들을 담은 리스트를 반환한다.
#     for j in range(1, 10):
#         if visited_column[j] == 0:
#             ans_list.append(j)
#     return ans_list
#
#
# def check_square(r, c):
#     visited_square = [0] * 10
#     ans_list = []
#     # 해당 3x3 사각형에서 없는 숫자를 확인한다.
#     r = (r // 3) * 3
#     c = (c // 3) * 3
#     for i in range(r, r + 3):
#         for j in range(c, c + 3):
#             if arr[i][j] != 0:
#                 visited_square[arr[i][j]] = 1
#     # 없는 숫자들을 담은 리스트를 반환한다.
#     for k in range(1, 10):
#         if visited_square[k] == 0:
#             ans_list.append(k)
#     return ans_list
#
#
# for i in range(9):
#     for j in range(9):
#         if arr[i][j] == 0:
#             row_list = check_row(i)
#             column_list = check_column(j)
#             square_list = check_square(i, j)
#
#             for row in row_list:
#                 if row in column_list and row in square_list:
#                     arr[i][j] = row
#
# for i in range(9):
#     print(' '.join(map(str, arr[i])))

