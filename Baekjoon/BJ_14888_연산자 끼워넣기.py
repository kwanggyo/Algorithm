import sys

def cal(idx):
    global max_ans, min_ans
    if idx == N-1:
        ans = nums[0]   # 초기값
        num = 1
        for k in check: # 인덱스로 +, -, *, / 확인
            if k == 0:
                ans += nums[num]
            elif k == 1:
                ans -= nums[num]
            elif k == 2:
                ans *= nums[num]
            else:
                ans = int(ans / nums[num])
            num += 1
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
    else:
        for i in range(4):  # 기존 수열과 다르게 +++ - * 에서 +++ 끼리 자리가 바꼈을때 계산 안하게 함
            if op[i]:
                op[i] -= 1
                check[idx] = i
                cal(idx + 1)
                op[i] += 1


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
check = [0] * (N - 1)
max_ans = -1000000000
min_ans = 1000000000

cal(0)

print(max_ans)
print(min_ans)