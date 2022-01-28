# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):

    def bfs(start):
        # 타겟이 단어 안에 없으면 변환 불가
        if target not in words:
            return 0
        # 있다면
        Q = deque()
        Q.append((start, 0))
        visited = [0] * len(words)
        while Q:
            word, cnt = Q.popleft()
            if word == target:
                return cnt
            for i in range(len(words)):
                if visited[i] == 1: continue
                change_word = words[i]
                same_cnt = 0
                # 알파벳이 몇개 변하는지
                for j in range(len(change_word)):
                    if change_word[j] == word[j]:
                        same_cnt += 1
                # 한개의 알파벳만 변환 가능일 때 넣어준다.
                if same_cnt == len(change_word) - 1:
                    visited[i] = 1
                    Q.append((change_word, cnt + 1))
                    visited[i] = 0

    answer = bfs(begin)

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))