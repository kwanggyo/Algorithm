a, b = map(int, input().split())
ans_a = a // b
ans_b = float(a) / b
# print(f'{ans_a} {round(ans_b, 2)}')     # 4MB, 32ms -> 80점
print('{} {:.2f}'.format(ans_a, ans_b))   # 4MB, 57ms -> 100점

# round(n, 자릿수)로 원하는 자리까지 반올림하여 표현 가능
# 음수를 넣으면 정수자리에서 반올림 ex) round(12345, -1) = 12340
# 엄격하게 준수하려면 format을 써야함 ex) round(3.10, 2) = 3.1
# print("{:.2f}".format(3.141592))
# print(format(3.141592, "1.2f"))
# ------ 추가 ------ #
# math.ceil(i) : 올림
# math.floor(i) : 내림
# math.trunc(i) : 버림