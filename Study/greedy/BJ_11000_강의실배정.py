# 끝 시간과 시작 시간을 비교해서 pop and append
# 참고 https://www.daleseo.com/python-heapq/
# 다시 볼 때 -> 정렬을 해주는 이유 heapq 활용 방법
import heapq
import sys
input = sys.stdin.readline
N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]
Q = [1]
room.sort(key=lambda x: x[0])
for i in range(N):
    if Q[0] <= room[i][0]:
        heapq.heappop(Q)
    heapq.heappush(Q, room[i][1])

print(len(Q))

# heapq priorityqueue -> 동시성 문제 heapq가 4배정도 빠름
# Thread safety를 보장하려면 priorityqueue
'''
6
1 3
1 2
2 4
3 5
4 5
2 3

4
1 2
3 4
4 5
3 5
'''