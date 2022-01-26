# https://programmers.co.kr/learn/courses/30/lessons/43165
# BFS
# 더하는 경우와 빼는 경우를 나누어서 BFS
# 프로그래머스 전역 변수 사용법 알아두기 !
# -> global과 nonlocal -> https://juhi.tistory.com/6 참고
# 다른 사람 풀이에서 재귀 풀이...참고..!


### BFS 풀이
from collections import deque

def solution(numbers, target):
    answer = 0
    N = len(numbers)
    Q = deque()
    Q.append((numbers[0], 0))
    Q.append((-1*numbers[0], 0))
    while Q:
        total, idx = Q.popleft()
        idx += 1
        if idx < N:
            Q.append((total + numbers[idx], idx))
            Q.append((total - numbers[idx], idx))
        else:
            if total == target:
                answer += 1
    return answer


# ### DFS 풀이
# def solution(numbers, target):
#     N = len(numbers)
#     answer = 0
#     def dfs(idx, result):
#         if idx == N:
#             if result == target:
#                 nonlocal answer
#                 answer += 1
#             return
#         else:
#             dfs(idx + 1, result + numbers[idx])
#             dfs(idx + 1, result - numbers[idx])
#     dfs(0, 0)
#
#     return answer


print(solution([1, 1, 1, 1, 1]	, 3))