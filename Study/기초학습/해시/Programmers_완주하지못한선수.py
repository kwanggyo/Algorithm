# https://programmers.co.kr/learn/courses/30/lessons/42576
# 해시

def solution(participant, completion):
    answer = ''
    participants = dict()
    # 참가한 사람들을 딕셔너리에 넣어준다.
    for name in participant:
        if name in participants:
            participants[name] += 1
        else:
            participants[name] = 1
    # 통과했다면 1 -> 0으로
    for name in completion:
        participants[name] -= 1

    for name, flag in participants.items():
        # 1인 사람 => 통과 못한 사람 출력
        if flag:
            answer = name
            break

    return answer


### 다른 풀이 -> Counter 공부 !! ###
# 딕셔너리는 값을 뺄 수 없지만 카운터 객체라서 가능하다.
# import collections
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]




print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))