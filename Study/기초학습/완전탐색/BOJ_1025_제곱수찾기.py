# https://www.acmicpc.net/problem/1025
# 등차 수열 -> 이동하는 간격을 변수로 for문을 돌려야한다.
# math.sqrt(number) % 1 == 0 인지 확인

import math

N, M = map(int, input().split())
numbers = [list(input()) for _ in range(N)]
ans = -1

for n in range(N):  # 행
    for m in range(M):  # 열
        # 1-N, 1-M으로 하면 안되는 이유 : 1 1 1 일 경우 돌아가지 않는다. -> 96% 틀렸습니다.
        for weight_n in range(-N, N):  # 행에서의 공차
            for weight_m in range(-M, M):  # 열에서의 공차
                # 두 공차가 모두 0이면 무한 루프
                if weight_n == 0 and weight_m == 0: continue
                step = 0
                x = n
                y = m
                value = ''
                # 입력받은 수들의 범위 안에서 가능한 수열 추출
                while (0 <= x < N) and (0 <= y < M):
                    # 숫자 조합
                    value += numbers[x][y]
                    step += 1

                    # 제곱수, 최댓값 확인
                    value_int = int(value)

                    if math.sqrt(value_int) % 1 == 0 and value_int > ans:
                        ans = value_int

                    # 공차를 적용한 다음 값
                    x = n + step * weight_n
                    y = m + step * weight_m

print(ans)