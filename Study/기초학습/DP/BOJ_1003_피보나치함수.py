# https://www.acmicpc.net/problem/1003
# DP
# DP를 사용 안하면 테케는 맞지만 시간초과 !
# 앞의 두 수에 들어간 0과 1의 개수를 각각 더해주면 된다.
# 30860KB, 76ms

def fibonacci(n):
    if n > 2:
        for i in range(3, n + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(f'{zero[n]} {one[n]}')


T = int(input())
for _ in range(T):
    N = int(input())
    zero = [1, 0, 1]
    one = [0, 1, 1]
    fibonacci(N)


# def fibonacci(n):
#     if n == 0:
#         ans[0] += 1
#         return 0
#     elif n == 1:
#         ans[1] += 1
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     ans = [0, 0]
#     fibonacci(N)
#     print(*ans)
