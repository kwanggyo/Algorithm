# https://www.acmicpc.net/problem/1062
# 완전탐색

# 시작 : anta, 끝 : tica -> a, n, t, i, c 5개는 무조건 사용해야 한다.
# 답은 맞는 것 같은데 시간초과,, -> 비트마스킹으로 풀어야한다고 함


def dfs(idx, cnt):
    global ans
    # 무조건 배워야하는 글자 5개를 빼고 배운 글자 수
    if cnt == K - 5:
        readcnt = 0 # 읽을 수 있는지.
        for word in words:
            check = True    # 읽을 수 있는지 체크 bool
            for w in word:
                # 읽을 수 없다면
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        ans = max(ans, readcnt)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


N, K = map(int, input().split())
words = []
for _ in range(N):
    words.append(input())

ans = 0
learn = [0] * 26    # 알파벳 갯수

# a, c, i, n, t는 무조건 배워야한다.
for alpha in ('a', 'c', 'i', 'n', 't'):
    learn[ord(alpha) - ord('a')] = 1

# k 가 5보다 작으면 어떤 단어도 배울 수 없다.
if K < 5:
    print(0)
# k 가 26이면 모든 단어를 배울 수 있다.
elif K == 26:
    print(N)
# 그 외에는 완탐.
else:
    dfs(0, 0)
    print(ans)


