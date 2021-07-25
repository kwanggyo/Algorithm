# https://www.acmicpc.net/problem/15661
# 전체에서 고른 숫자들을 빼고 계산해야한다.
# 2개 이상의 조합을 가지고 판단
# 132232, 2304ms // PyPy3

def comb(idx, start, r):
    global ans
    if idx == r:
        sum1 = 0
        sum2 = 0
        pick2 = base - pick
        for val in pick:
            for j in pick:
                sum1 += stat[val][j]
        for val2 in pick2:
            for k in pick2:
                sum2 += stat[val2][k]
        if ans > abs(sum1 - sum2):
            ans = abs(sum1 - sum2)
    else:
        for i in range(start, N):
            pick.add(i)
            comb(idx + 1, i + 1, r)
            pick.remove(i)


N = int(input())
stat = [list(map(int, input().split())) for _ in range(N)]
base = set(i for i in range(N))
pick = set()
ans = 987654321

for i in range(2, N // 2 + 1):
    if ans == 0: break
    comb(0, 0, i)

print(ans)