# https://www.acmicpc.net/problem/1541
# Greedy
# 30864KB, 76ms
# -가 나온다면 다음 -가 나오가나 숫자가 끝날 때까지 더해서 뺀다
# -> -가 나오는 순간부터 뒤에 전부를 더해서 빼면 된다 !


expression = input()
plus_minus = {'+', '-'}
numbers = []
operator = []
tmp = ''
# 연산자와 피연산자 구분
for num in expression:
    if num in plus_minus:
        numbers.append(int(tmp))
        tmp = ''
        operator.append(num)
    else:
        tmp += num
numbers.append(int(tmp))

ans = numbers[0]
ans_tmp = 0
for i in range(len(operator)):
    if operator[i] == '-':
        ans_tmp += sum(numbers[i + 1:])
        break
    else:
        ans += numbers[i + 1]
ans -= ans_tmp

print(ans)




