# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
# 소수 : 1을 제외하고 제곱급으로 나오는 수의 정수값이하의 수로 나누었을 때 나누어지면 안된다.

from itertools import permutations

def solution(numbers):
    check = set()   # 중복 체크를 위한 set
    answer = 0
    for i in range(1, len(numbers) + 1):
        for val in permutations(numbers, i):
            isNumber = True
            num = int(''.join(val))
            if num in check: continue
            else:
                check.add(num)
            # 소수 체크
            if num < 2: continue
            for j in range(2, int(num**0.5) + 1):
                if num % j == 0:
                    isNumber = False
                    break
            if isNumber:
                answer += 1
    return answer
