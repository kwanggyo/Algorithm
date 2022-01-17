# https://programmers.co.kr/learn/courses/30/lessons/42746
# 정렬
# Tip : 문자열 비교 연산은 첫번쨰 인덱스부터 ascii 숫자로 바꿔서 비교한다.
# 참고 : https://wikidocs.net/109303 -> functools.cmp_to_key 활용해서 푸는 방법이 있다..!

# 순열로 만들 수 있는 경우의 수를 전부 리스트에 집어 넣고 최댓갑 출력
# -> 시간 초과
# from itertools import permutations
#
# def solution(numbers):
#     ans_list = []
#     for i in permutations(numbers, len(numbers)):
#         number = ''.join(map(str, i))
#         ans_list.append(number)
#     ans_list.sort(reverse=True)
#     answer = ans_list[0]
#     return answer




def solution(numbers):
    numbers = list(map(str, numbers))
    # 각 문자열을 반복해서 3자리수로 맞춰준다.
    numbers.sort(key=lambda x : x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer




# # functools.cmp_to_keys를 활용한 풀이법
# import functools
#
# def comparator(a,b):
#     t1 = a+b
#     t2 = b+a
#     return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
#
# def solution(numbers):
#     n = [str(x) for x in numbers]
#     n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
#     answer = str(int(''.join(n)))
#     return answer