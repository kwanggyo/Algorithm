# https://www.acmicpc.net/problem/1092
# Greedy
# PyPy3 : 125416KB, 3244ms -> Python 시간초과
# Python : 30864KB, 360ms

import sys
input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

# 내림차순 정렬
cranes.sort(reverse=True)
boxes.sort(reverse=True)

time = 0 # 시간
checked = [0] * M # 박스를 옮겼는지 여부
count = 0 # 옮긴 박스의 개수
positions = [0] * N # 크레인에 들어가 있는 박스의 번호

if max(cranes) < max(boxes):    # 옮길 수 없는 경우
    print(-1)
else:
    while count < len(boxes):
        for i in range(N):  # 크레인에 대하여
            while positions[i] < len(boxes):
                # 아직 안 옮긴 박스 중에서 옮길 수 있는 박스를 만날 때까지 반복
                if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
                    checked[positions[i]] = 1   # 옮김 표시
                    positions[i] += 1   # 다음 박스를 옮기면 된다.
                    count += 1
                    break
                positions[i] += 1   # 이미 옮긴 박스이므로 다음 박스
        time += 1
    print(time)


#### PyPy3 풀이 ####
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# cranes = list(map(int, input().split()))
# M = int(input())
# boxes = list(map(int, input().split()))
#
# cranes.sort(reverse=True)
# boxes.sort(reverse=True)
#
# if boxes[0] > cranes[0]:
#     print(-1)
# else:
#     time = 0
#     while boxes:
#         if not boxes:
#             break
#         for crane in cranes:
#             for box in boxes:
#                 if crane >= box:
#                     boxes.remove(box)
#                     break
#         time += 1
#
#     print(time)