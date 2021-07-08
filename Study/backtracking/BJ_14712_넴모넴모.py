# 2^(NxM)의 개수(비트연산) - 4개씪 뭉쳐있는 곳을 빼자 !
# https://www.acmicpc.net/problem/14712
# 시간초과

N, M = map(int, input().split())
total = 1 << (N*M)
ans_cnt = 0
for i in range(1 << (N*M)):
    cnt = 0 # 개수 카운팅 -> 4개가 넘어야 판별할거임
    Nemo_li = []
    for j in range(N*M):
        if i & (1 << j):
            cnt += 1
            Nemo_li.append(j)
    if cnt >= 4:
        for val in Nemo_li:
            if cnt >= 4:
                if (val + 1) % M:
                    if (val + 1) in Nemo_li and (val + M) in Nemo_li and (val + M + 1) in Nemo_li:
                        ans_cnt += 1
                        break
            cnt -= 1
print(total - ans_cnt)
