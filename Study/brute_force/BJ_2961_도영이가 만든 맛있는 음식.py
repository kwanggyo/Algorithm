# 부분집합 구해서 계산
# 29200KB 76ms

N = int(input())
taste = [list(map(int, input().split())) for _ in range(N)]
ans = 1000000000
flag = False
for i in range(1 << N):
    sour = 1
    bitter = 0
    for j in range(N):
        if i & (1 << j):
            sour *= taste[j][0]
            bitter += taste[j][1]
            flag = True
    if flag:
        res = abs(sour - bitter)
        if ans > res:
            ans = res
        flag = False

print(ans)