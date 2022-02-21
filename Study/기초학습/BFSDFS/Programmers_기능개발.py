# https://programmers.co.kr/learn/courses/30/lessons/42586
# 스택/큐

# 끝내려면 필요한 날짜를 정렬하고 정렬한 배열을 처음부터 돌면서 개수를 답에 저장

def solution(progresses, speeds):
    answer = []
    count = []
    # 걸리는 날짜 정리
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] != 0:
            count.append((100 - progresses[i]) // speeds[i] + 1)
        else:
            count.append((100 - progresses[i]) // speeds[i])

    max_day = count[0]   # 기준 날짜
    day = 1
    for cnt in count[1:]:
        if cnt > max_day:
            answer.append(day)
            max_day = cnt
            day = 1
        else:
            day += 1
    answer.append(day)

    return answer


print(solution([93, 30, 55], 	[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([96,94],[3,3])) # 11번 테케 반례


### 정답코드 참고 ###
# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]