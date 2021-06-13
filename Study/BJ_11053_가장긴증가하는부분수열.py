# 29200KB, 216ms
A = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(A)]  # 기본적으로 1의 길이를 가지므로 초기값 1
for i in range(A):
    for j in range(i):
        if arr[i] > arr[j]:     # 증가하는 부분수열
            dp[i] = max(dp[i], dp[j] + 1)   # 기존의 dp 값과 비교

print(max(dp))