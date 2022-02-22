# https://programmers.co.kr/learn/courses/30/lessons/42587
# 스택/큐
# 다시 풀어보기

from collections import deque

def solution(priorities, location):
    answer = 0
    # 구해야하는 location을 고정하기 위해 idx를 같이 넣어줌
    priorities = deque([(val, idx) for idx, val in enumerate(priorities)])
    # 구할 때까지 반복
    while len(priorities):
        number, now_location = priorities.popleft()
        # 마지막 수가 아니어야 하고 꺼내온 것이 최댓값이 아니면
        if priorities and max(priorities)[0] > number:
            priorities.append((number, now_location))
        # 마지막 수 이거나 꺼내온 것이 최댓값이라면
        else:
            answer += 1
            # 구하려는 인덱스라면
            if location == now_location:
                break

    return answer


print(solution([2, 2, 4, 2, 3, 2], 1))
print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))