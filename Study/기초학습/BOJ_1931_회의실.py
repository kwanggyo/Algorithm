# https://www.acmicpc.net/problem/1931

# 회의 시작 시간과 끝나는 시간을 튜플로 리스트에 저장
# 인풋으로 받은 리스트를 시작 시간 순으로 정렬
# 처음 푼 코드 : 시간초과 -> N의 개수가 10만이기 때문에 for문 2개 사용하면 안됨
# 46276KB, 284ms

import sys
input = sys.stdin.readline

N = int(input())
meeting = []
for _ in range(N):
    s, e = map(int, input().split())
    meeting.append((s, e))

# 시작 시간으로 정렬
meeting = sorted(meeting, key = lambda  x : x[0])
# 종료 시간을 기준으로 한번 더 정렬
# [(1, 3) (0, 3)] 이런식으로 들어가 있는 것을 바로 정렬하면 그대로 정렬된다
# x[0]로 정렬과정을 한번 거치면 -> [(0, 3), (1, 3)] 으로 정렬된다.
meeting = sorted(meeting, key = lambda  x : x[1])

end_time = meeting[0][1]
cnt = 1
for lecture in meeting[1 : N]:
    # 강의의 시작 시간이 이전 강의 종료시간보다 빠르면
    if lecture[0] < end_time: continue
    # 강의 시간이 겹치지 않고 이어갈 수 있다면
    else:
        end_time = lecture[1]
        cnt += 1
print(cnt)

######### 시간초과 코드 #########
# ans = []
#
# for i in range(N):
#     S, E = meeting[i][0], meeting[i][1]
#     length = 1
#     for j in range(i + 1, N):
#         s_time, e_time = meeting[j][0], meeting[j][1]
#         # 이전 강의가 끝나는 시간보다 시작 시간이 빠르면 종료
#         if s_time < E:
#             continue
#         # 다음 강의를 이어서 할 수 있다면
#         else:
#             length += 1
#             E = e_time
#     ans.append(length)
#
# print(max(ans))

'''
# 아래 코드를 실행시켜보면 정렬을 2번하는 이유을 알 수 있다.
arr = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]
arr1 = sorted(arr, key = lambda x : x[0])
arr2 = sorted(arr, key = lambda x : x[1])
arr3 = sorted(arr1, key = lambda x : x[1])

print(arr)
print(arr1)
print(arr2)
print(arr3)
'''
