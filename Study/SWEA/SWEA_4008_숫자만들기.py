import sys

def cal(idx):
    global max_val, min_val
    if idx == N - 1:
        ans = nums[0]
        num = 1
        for o in check:
            if o == 0:
                ans += nums[num]
            elif o == 1:
                ans -= nums[num]
            elif o == 2:
                ans *= nums[num]
            else:
                ans = int(ans / nums[num])
            num += 1
        max_val = max(max_val, ans)
        min_val = min(min_val, ans)
    else:
        for i in range(4):  # 경우의 수 구하기 -> 순열에서 중복 빼줌
            if op[i] != 0:
                op[i] -= 1
                check[idx] = i
                cal(idx + 1)
                op[i] += 1

T = int(sys.stdin.readline())
for tc in range(1, T + 1):
    N = int(sys.stdin.readline())
    # 연산자 +, -, *, /
    op = list(map(int, sys.stdin.readline().split()))
    nums = list(map(int, sys.stdin.readline().split()))
    check = [0] * (N - 1)
    max_val = -100000001
    min_val = 100000001
    cal(0)

    print('#{} {}'. format(tc, max_val - min_val))