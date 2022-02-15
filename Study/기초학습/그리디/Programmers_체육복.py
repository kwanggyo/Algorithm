# https://programmers.co.kr/learn/courses/30/lessons/42862
# Greedy
# https://devpouch.tistory.com/110 -> remove 하는 경우 참고!

def solution(n, lost, reserve):
    answer1 = n - len(lost)
    answer2 = n - len(lost)
    lost.sort()
    reserve.sort()
    # 여분을 가져왔지만 잃어버린 사람을 우선적으로 빼줘야한다!
    for num1 in lost[:]:
        for num2 in reserve[:]:
            if num1 < num2:
                break
            if num1 == num2:
                lost.remove(num1)
                reserve.remove(num1)
                answer1 += 1
                answer2 += 1
                break

    reserve2 = reserve.copy()   # 2가지 경우를 비교하기 위해
    # 앞에서 부터 비교하는 경우
    for num1 in lost[:]:
        for num2 in reserve[:]:
            if num1 + 1 < num2:
                break
            if num1 - 1 == num2:
                reserve.remove(num2)
                answer1 += 1
                break
            elif num1 + 1 == num2:
                reserve.remove(num2)
                answer1 += 1
                break
    # 뒤에서부터 비교하는 경우
    for num1 in lost[:]:
        for num2 in reserve2[:]:
            if num1 + 1 < num2:
                break
            if num1 + 1 == num2:
                reserve2.remove(num2)
                answer2 += 1
                break
            elif num1 - 1 == num2:
                reserve2.remove(num2)
                answer2 += 1
                break
    # 둘 중 큰 값으로 결정!! (테케 7번 관련)
    answer = max(answer1, answer2)
    return answer


print(solution(5, [2, 4], [1, 3, 5]))
# print(solution(5, [2, 4], [3]))
# print(solution(3, [3], [1]))
# print(solution(5, [4, 2], [2, 3]))
# print(solution(5, [3], [3]))
# print(solution(10, [2, 4], [1, 2, 5]))
# print(solution(3, [1, 2], [2, 3]))
# print(solution(30, [1, 2, 7, 9, 10, 11, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27], [1, 2, 3, 4, 5,
#          6, 7, 8, 9, 10,
#          11, 12, 13, 14, 15,
#          16, 17, 20, 22, 23,
#          24, 25, 26, 27, 28]))




##### 참고 코드 ##### -> !!!
# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)