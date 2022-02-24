# https://programmers.co.kr/learn/courses/30/lessons/42584
# 스택/큐

from collections import deque

def solution(prices):
    answer = []
    Q = deque(prices)
    while Q:
        price = Q.popleft()
        sec = 0
        for q in Q:
            sec += 1
            # 비교하는 가격보다 작다면 떨어진 것
            if price > q:
                break
        answer.append(sec)

    return answer


### 참고 코드 ###
# # prices = [1, 2, 3, 2, 3, 1] return [5, 4, 1, 2, 1, 0]
# def solution(prices):
#     length = len(prices)
#
#     # answer을 max값으로 초기화
#     answer = [i for i in range(length - 1, -1, -1)]
#
#     # 주식 가격이 떨어질 경우 찾기
#     stack = [0]
#     for i in range(1, length):
#         while stack and prices[stack[-1]] > prices[i]:
#             j = stack.pop()
#             answer[j] = i - j
#         stack.append(i)
#     return answer


### 다른 풀이 참고 코드 ###
# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break
#     return answer


print(solution([1, 2, 3, 2, 3]))