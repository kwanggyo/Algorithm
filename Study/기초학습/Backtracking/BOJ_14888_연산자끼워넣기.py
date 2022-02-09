# https://www.acmicpc.net/problem/14888
# Backtracking
# 30864KB, 112ms

import sys
input = sys.stdin.readline

def cal(total, cnt):
    # 연산자를 N - 1개 쓴 것 => 계산 끝
    if cnt == N - 1:
        ans.append(total)
    else:
        for i in range(4):
            if operator[i] != 0:
                operator[i] -= 1
                if i == 0:
                    cal(total + numbers[cnt+1], cnt + 1)
                elif i == 1:
                    cal(total - numbers[cnt+1], cnt + 1)
                elif i == 2:
                    cal(total * numbers[cnt+1], cnt + 1)
                # 나눗셈 계산 C++14 방식
                elif i == 3:
                    if total < 0:
                        cal((abs(total) // numbers[cnt+1]) * -1, cnt + 1)
                    else:
                        cal(total // numbers[cnt + 1], cnt + 1)
                operator[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
# +, -, *, //
operator = list(map(int, input().split()))
ans = []
cal(numbers[0], 0)
print(max(ans))
print(min(ans))