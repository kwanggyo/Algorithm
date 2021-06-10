a, b = map(float, input().split())      # 실수를 받으려면 float으로 !
print(f'{int(a * b)} {int(a) * int(b)}')    # 곱한 후에 정수로 바꿔주는 것과 정수로 바꾼 후(그 수를 넘지 않는 최댓값) 곱의 차이

# 4MB 71ms