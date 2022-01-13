# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3
# 완전탐색
# Yellow = a * b 이고 a >= b인 사각형 구하기
# Brown = 2(a + b) + 4인 것 구하기


def solution(brown, yellow):
    answer = []
    # 확인할 범위 정해주기
    R = (brown - 4) // 2 if (brown - 4) // 2 < yellow else yellow
    for i in range(1, R + 1):
        if yellow % i == 0:
            if i >= yellow // i:
                x = i
                y = yellow // i
            else:
                x = yellow // i
                y = i
            if 2*(x + y) + 4 == brown:
                answer.append(x+2)
                answer.append(y+2)
                break
    return answer
