# https://www.acmicpc.net/problem/12919
# 완전탐색 + 백트래킹
# 30864KB, 72ms

# S를 P로 바꾸려는 경우 시간초과
# P를 S로 바꿔야한다

def isPossible(t):
    global ans
    if len(t) == len(S):
        if t == S:
            ans = 1
        return

    # B를 추가하고 뒤집은 경우
    if t[0] == 'B':
        t = t[::-1]
        t.pop()
        isPossible(t)
        t.append('B')
        t = t[::-1]
    # A를 추가한 경우
    if t[-1] == 'A':
        t.pop()
        isPossible(t)
        t.append('A')


S = list(input())
T = list(input())
ans = 0
isPossible(T)
print(ans)








# ### S -> P 14% 시간초과 ###
# def isPossible(s, t):
#     global ans
#     if len(s) == len(t):
#         if s == t:
#             ans = 1
#         return
#     isPossible(s + 'A', t)
#     As = s + 'B'
#     Rs = As[::-1]
#     isPossible(Rs, t)
#
# S = input()
# T = input()
# ans = 0
# isPossible(S, P)
# print(ans)