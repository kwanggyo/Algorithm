# https://programmers.co.kr/learn/courses/30/lessons/42746
# 정렬

def solution(numbers):
    numbers_to_str = []
    for number in numbers:
        numbers_to_str.append(str(number))
    numbers_to_str.sort(reverse=True)
    answer = ''.join(numbers_to_str)
    return answer

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))