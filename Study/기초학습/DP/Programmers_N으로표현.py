# https://programmers.co.kr/learn/courses/30/lessons/42895
# DP

# 3 -> dp[1]과 dp[2]를 연산, 4 -> dp[1]과 dp[3], dp[2]와 dp[2]를 연산 ...
# 시간초과, 틀렸습니다 -> str로 바꿔주는 작업과 중복되는 값 많고 중간 연산에서 문제가 생긴 것 같다.
# 같은 생각으로 푼 코드를 참고

def solution(N, number):
    dp = [0, [N]]  # 가능한 수를 저장한다.
    if N == number:  # 주어진 수와 구하려는 수가 같으면 답은 1
        return 1
    for i in range(2, 9):  # dp[8]까지 구해준다.
        case = []  # 횟수에 해당하는 수를 저장하고 dp에 append 해줄 예정
        case.append(int(str(N) * i))  # 기본적으로 같은 수를 연속으로 적은 수를 넣어준다.
        for i_half in range(1, i//2+1):  # 숫자의 조합으로 i를 만들어야하는데 절반을 넘어가면 중복된 것이므로 절반까지만(뺼셈과 나눗셈만 따로 해준다)
            for x in dp[i_half]:
                for y in dp[i-i_half]:  # x와 y를 더하면 i 가 되도록 만든 수다.
                    # 각 사칙연산 결과를 더한다.
                    case.append(x + y)
                    case.append(x - y)
                    case.append(y - x)  # 따로 해준 부분
                    case.append(x * y)
                    if y != 0:
                        case.append(x / y)
                    if x != 0:  # 따로 해준 부분
                        case.append(y / x)   # //로 해주면 틀림..(테케8번) -> 위 if y 부분은 //로 해줘도 됨 => 왜??
                                             # ex) 25 == 25.0 => True //으로 하면 몫만 나오기 때문에 예외가 있는듯 하다.
            if number in case:
                return i
            dp.append(case)  # 다음 계산을 위해 dp에 넣어준다.
    return -1  # 답이 없는 경우


##### 실패 코드 #####
# def solution(N, number):
#     answer = -1
#     dp = [[] for _ in range(8)]
#     dp[0] = str(N)
#     dp[1] = [str(N) + '+' + str(N), str(N) + '-' + str(N), str(N) + '*' + str(N), str(N) + '//' + str(N), str(N)*2]
#     if number == int(dp[0]):
#         answer = 1
#         return answer
#     for val in dp[1]:
#         if eval(val) == number:
#             answer = 2
#             return answer
#
#     for i in range(2, 8):
#         for j in dp[i - 1]:
#             dp[i].append('(' + j + '+' + str(N) + ')')
#             dp[i].append(j + '+' + str(N))
#             dp[i].append('(' + j + '-' + str(N) + ')')
#             dp[i].append(j + '-' + str(N))
#             dp[i].append(j + '*' + str(N))
#             dp[i].append('(' + j + '*' + str(N) + ')')
#             dp[i].append(j + '//' + str(N))
#             dp[i].append('(' + j + '//' + str(N) + ')')
#         dp[i].append(str(N) * (i+1))
#
#         for k in dp[i]:
#             if eval(k) == number:
#                 answer = i + 1
#                 return answer
#
#     return answer


print(solution(5, 12))
print(solution(2, 11))
print(solution(5, 5))
print(solution(1, 1121))
print(solution(5, 26))