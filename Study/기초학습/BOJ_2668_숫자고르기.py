# https://www.acmicpc.net/problem/
# 32396KB, 88ms
# DFS

# 1. 1부터 ~ N + 1까지 해당하는 값을 다시 인덱스로 타고 간다.
# 2. 타고 가다가 처음 시작한 인덱스 값이 나오게 되면 멈춘다.
# 3. 이때 지나갔던 값들을 방문 체크 하고 답에 추가 한다.

from collections import deque

def series():
    for i in range(1, N + 1):
        end = i
        Q = deque()
        Q.append(i)
        visited[i] = 1
        check = set()
        while Q:
            idx = Q.popleft()
            start = arr[idx]
            # 지나왔던 갑이 나오면 PASS
            if start in check: break
            # 처음 시작했던 값이 나오면 정답에 추가해준다.
            if start == end:
                ans.append(end)
                for val in check:
                    visited[val] = 1
                    ans.append(val)
                break
            # 방문했던(정답을 체크했던) 것이 나오면 PASS
            if visited[start] == 1: break
            check.add(start)
            Q.append(start)


N = int(input())
arr = [0] * (N + 1)
for i in range(1, N + 1):
    arr[i] = int(input())
visited = [0] * (N + 1)
ans = []

series()
ans.sort()
print(len(ans))
for val in ans:
    print(val)
