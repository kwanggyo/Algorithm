# https://www.acmicpc.net/problem/3980
# 하나의 포지션을 선택하고 해당하는 능력치를 더해나간다.
# 방문 체크를 통해 포지션이 겹치지 않도록 한다.

import sys
input = sys.stdin.readline

def getMin(idx, sum):
    global ans
    if idx == 11:
        if ans < sum:
            ans = sum
        return
    for i in range(11):
        if check[i] == 1 or ability[idx][i] == 0: continue
        check[i] = 1
        getMin(idx + 1, sum + ability[idx][i])
        check[i] = 0


C = int(input())
for c in range(C):
    ability = [list(map(int, input().split())) for _ in range(11)]
    check = [0] * 11
    ans = 0
    getMin(0, 0)
    print(ans)
