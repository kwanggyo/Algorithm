# https://programmers.co.kr/learn/courses/30/lessons/42860
# 그리디
# A : 65, Z : 90
# 74.1점 -> 실패하는 테스트케이스가 있음

def solution(name):
    answer = 0
    min_move = len(name) - 1    # 좌 -> 우로 끝까지 갈 때

    # 끝이 A로 끝나는 경우
    while name[min_move] == 'A' and min_move > 0:
        min_move -= 1

    # 전부 A인 경우
    if (min_move < 0):
        return answer

    for idx, x in enumerate(name):
        # 위, 아래로 움직이는 횟수
        answer += min(ord(x) - ord('A'), ord('Z') - ord(x) + 1)

        # 좌우로 움직이는 횟수
        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min(min_move, idx + (idx + len(name)) - next)

    answer += min_move
    return answer
