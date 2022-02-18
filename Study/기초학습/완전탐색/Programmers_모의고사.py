# https://programmers.co.kr/learn/courses/30/lessons/42840
# 완전탐색
# 방법 생각 않나서 if로 완탐..

# 1, 2, 3, 4, 5, 1, 2, 3, 4, 5,
# 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5,
# 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,

def solution(answers):
    answer = []
    score = [0] * 3
    for i in range(len(answers)):
        # 해당 번호에 적은 수포자 친구들의 답
        one = (i % 5) + 1

        if i % 2 == 0:
            two = 2
        elif i % 8 == 1:
            two = 1
        elif i % 8 == 3:
            two = 3
        elif i % 8 == 5:
            two = 4
        elif i % 8 == 7:
            two = 5

        if i % 10 == 0 or i % 10 == 1:
            three = 3
        elif i % 10 == 2 or i % 10 == 3:
            three = 1
        elif i % 10 == 4 or i % 10 == 5:
            three = 2
        elif i % 10 == 6 or i % 10 == 7:
            three = 4
        elif i % 10 == 8 or i % 10 == 9:
            three = 5

        # 정답 확인
        if one == answers[i]:
            score[0] += 1
        if two == answers[i]:
            score[1] += 1
        if three == answers[i]:
            score[2] += 1

    # 답에 넣기
    max_score = max(score)
    for idx, val in enumerate(score):
        if val == max_score:
            answer.append(idx + 1)

    return answer



print(solution([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))


##### 참고할 코드 #####
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []
#
#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1
#
#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)
#
#     return result