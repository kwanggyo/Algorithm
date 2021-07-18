# 문제 : https://www.acmicpc.net/problem/11055
# n번째 인덱스까지 최댓값을 갱신해서 저장 -> DP
# 29200KB, 220ms
N = int(input())
arr = list(map(int, input().split()))
DP = [x for x in arr]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            DP[i] = max(DP[i], DP[j] + arr[i])
print(max(DP))