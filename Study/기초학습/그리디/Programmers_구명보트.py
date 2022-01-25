# https://programmers.co.kr/learn/courses/30/lessons/42885
# 그리디
# 제일 무거운 사람과 제일 가벼운 사람이 같이 가는 방식

def solution(people, limit):
    answer = 0
    P = len(people)
    people.sort()
    s = 0
    for i in range(P - 1, -1, -1):
        if s > i:
            break
        if people[s] + people[i] > limit:
            answer += 1
            continue
        s += 1
        answer += 1
    return answer


# print(solution([70, 50, 80, 50],100))
# print(solution([70, 80, 50], 100))
