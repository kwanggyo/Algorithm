# https://programmers.co.kr/learn/courses/30/lessons/43164
# DFS
# 테케 1, 2번 런타임에러

def solution(tickets):
    answer = []
    airport = dict()
    for ap in tickets:
        if ap[0] in airport.keys():
            airport[ap[0]].append(ap[1])
        else:
            airport[ap[0]] = [ap[1]]
    # 알파벳 순으로 정렬한다.
    for key in airport.keys():
        airport[key].sort()

    ans = ['ICN']

    def dfs(idx, val):
        if idx == len(tickets):
            answer.append(ans)
        else:
            if len(airport[val]) == 0:
                return
            for a in airport[val]:
                airport[val].pop(0)
                ans.append(a)
                dfs(idx + 1, a)
    dfs(0, 'ICN')
    answer = answer[0]

    return answer



print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))