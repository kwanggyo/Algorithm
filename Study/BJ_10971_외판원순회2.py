# 완전탐색 후 가지치기
# 29200KB, 92ms

def search_min_cost(idx, li, cost, now):
    global min_cost
    if min_cost < cost:     # 가지치기
        return
    if idx == N-1:
        if arr[now][0] != 0:    # 마지막 돌아가는 부분! 여기를 생각안해서 틀렸었음
            res = cost + arr[now][0]    # 돌아가는 길이 있으면 더해주고 최솟값 비교
            if min_cost > res:
                min_cost = res
        else:
            return

    else:
        for i in range(N):
            if i in visited or li[i] == 0:  # 0이면 길이 없다.
                continue
            else:
                visited.add(i)
                search_min_cost(idx + 1, arr[i], cost + li[i], i)
                visited.remove(i)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_cost = 9876543210
visited = set()     # 방문 체크
visited.add(0)
search_min_cost(0, arr[0], 0, 0)
print(min_cost)


# 반례
# 4
# 0 1 2 0
# 1 0 2 0
# 0 0 0 3
# 0 2 0 0
# 1 -> 2 -> 3 -> 4 -> 1이 불가능
# 1 -> 3 -> 4 -> 2 -> 1로 와야한다.