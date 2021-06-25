import sys

def search():
    global ans
    # global cnt
    for i in range(N):
        num_dict = {}
        for j in range(i, N):
            # cnt += 1
            if N - i <= ans:
                return
            if arr[j] not in num_dict:
                num_dict[arr[j]] = 1
            else:
                num_dict[arr[j]] += 1
                if num_dict[arr[j]] == M + 1:
                    if (j - i) > ans:
                        ans = j - i
                    break

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
cnt = 0
search()
print(ans)
# print(cnt)

