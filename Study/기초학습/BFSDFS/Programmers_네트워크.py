# https://programmers.co.kr/learn/courses/30/lessons/43162
# DFS

def solution(n, computers):
    answer = 0
    visited = [0] * n

    def dfs(start):
        S = []
        S.append(start)
        visited[start] = 1
        while S:
            node = S.pop()
            for i in range(n):
                if node == i: continue
                if visited[i] == 0 and computers[node][i] == 1:
                    visited[i] = 1
                    S.append(i)

    for j in range(n):
        if visited[j] == 0:
            dfs(j)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))