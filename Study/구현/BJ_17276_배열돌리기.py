# 보이는데로 구현
# 문제 : https://www.acmicpc.net/problem/17276
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=dudwo567890&logNo=130163015383
# 63804KB, 4768ms
import copy
T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    arr = [list(input().split()) for _ in range(N)]
    turn = abs(D // 45)
    ans = [[0] * N for _ in range(N)]
    ans = copy.deepcopy(arr)
    cnt = 0
    if D >= 0:
        while cnt < turn:
            for i in range(N):
                ans[i][N//2] = arr[i][i]
                ans[i][N-1-i] = arr[i][N//2]
                ans[N//2][i] = arr[N-1-i][i]
                ans[i][i] = arr[N//2][i]
            cnt += 1
            arr = copy.deepcopy(ans)
    else:
        while cnt < turn:
            ans = copy.deepcopy(arr)
            for i in range(N):
                ans[i][N//2] = arr[i][N-1-i]
                ans[i][N-1-i] = arr[N//2][N-1-i]
                ans[N//2][i] = arr[i][i]
                ans[i][i] = arr[i][N//2]
            cnt += 1
            arr = copy.deepcopy(ans)

    for i in range(N):
        print(' '.join(ans[i]))