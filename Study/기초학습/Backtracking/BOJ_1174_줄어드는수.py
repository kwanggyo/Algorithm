# https://www.acmicpc.net/problem/1174
# Backtracking
# 30864KB, 76ms

# 0 1 2 3 4 5 6 7 8 9 10 20 21 30 31 32 40 41 42

from itertools import combinations

N = int(input())
ans = []
base = [i for i in range(10)]
for digit in range(1, 11):
    # 조합을 통해서 중복 되지 않도록 숫자를 뽑는다.
    numbers = list(combinations(base, digit))
    for number in numbers:
        # 오름차순으로 정렬한 후
        number = sorted(number)
        num = 0
        # 인덱스에 따라 자릿수를 곱해주면 줄어드는 수가 나온다.
        for i in range(digit):
            num += (10**i) * number[i]
        ans.append(num)
# 나온 줄어드는 수를 오름차순으로 정렬
ans.sort()

if len(ans) >= N:
    print(ans[N - 1])
else:
    print(-1)



# # 시간초과 -> 0 ~ 9876543210까지 돌리니까 당연함..
# N = int(input())
# numbers = []
# i = 0
# while len(numbers) < N:
#     if i < 10:
#         numbers.append(i)
#     else:
#         number = str(i)
#         L = len(number)
#         flag = True
#         for j in range(L-1):
#             if number[j] <= number[j + 1]:
#                 flag = False
#                 break
#         if flag == True:
#             numbers.append(i)
#     i += 1
#     if i > 9876543210:
#         break
#
# if len(numbers) == N:
#     print(numbers[N-1])
# else:
#     print(-1)