# https://programmers.co.kr/learn/courses/30/lessons/42883
# 그리디

def solution(number, k):
    answer = ''
    numbers = list(map(int, number))
    cnt = 0
    while k > 1:
        max_num = -1
        max_idx = 0
        # 앞에서 k개 만큼을 비교한다.
        for i in range(k):
            if max_num < numbers[i]:
                max_num = numbers[i]
                max_idx = i
        # 제일 큰 수를 답에 넣어주고
        answer += str(max_num)
        k -= max_idx
        # 해당하는 인덱스를 통해 슬라이싱한다.
        if max_idx == len(numbers): # k == 0이 되기 떄문에
            numbers = numbers[max_idx:]
        else:
            numbers = numbers[max_idx + 1:]
    if k == 1:
        if numbers[0] >= numbers[1]:
            answer += str(numbers[0])
            numbers = numbers[2:]
        else:
            numbers = numbers[1:]

    for j in range(len(numbers)):
        answer += str(numbers[j])
    return answer


print(solution('424', 1))
print(solution('1924', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))