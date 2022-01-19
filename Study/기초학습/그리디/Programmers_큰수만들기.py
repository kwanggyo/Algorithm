# https://programmers.co.kr/learn/courses/30/lessons/42883
# 그리디
# 다시 풀어보기

def solution(number, k):
    # stack에 입력값을 순서대로 삽입
    stack = [number[0]]
    for num in number[1:]:
        # 들어오는 값이 stack 값보다 크면, 기존의 값을 제거하고 새로운 값으로 바꿈
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # 값을 한개 빼서 k는 1이 제거
            k -= 1
            # 내부의 값을 제거
            stack.pop()
        # 새로운 값을 삽입
        stack.append(num)
    # 만일 충분히 제거하지 못했으면 남은 부분은 단순하게 삭제
    # 이렇게 해도 되는 이유는 이미 큰 수부터 앞에서 채워넣었기 때문
    if k != 0:
        stack = stack[:-k]
    answer = ''.join(stack)
    return answer


# def solution(number, k):
    # answer = ''
    # numbers = list(map(int, number))
    # cnt = 0
    # while k > 1:
    #     max_num = -1
    #     max_idx = 0
    #     # 앞에서 k개 만큼을 비교한다.
    #     for i in range(k):
    #         if max_num < numbers[i]:
    #             max_num = numbers[i]
    #             max_idx = i
    #     # 제일 큰 수를 답에 넣어주고
    #     answer += str(max_num)
    #     k -= max_idx
    #     # 해당하는 인덱스를 통해 슬라이싱한다.
    #     if max_idx == len(numbers): # k == 0이 되기 떄문에
    #         numbers = numbers[max_idx:]
    #     else:
    #         numbers = numbers[max_idx + 1:]
    # if k == 1:
    #     if numbers[0] >= numbers[1]:
    #         answer += str(numbers[0])
    #         numbers = numbers[2:]
    #     else:
    #         numbers = numbers[1:]
    #
    # for j in range(len(numbers)):
    #     answer += str(numbers[j])
    # return answer


# print(solution('10', 1)) # k != 0 반례
# print(solution('424', 1))
# print(solution('1924', 2))
# print(solution('1231234', 3))
# print(solution('4177252841', 4))