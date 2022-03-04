# https://www.acmicpc.net/problem/2661
# 백트래킹
# 30864KB, 84ms

# 연속으로 같은 숫자가 나오면 안된다.
# 어떻게 판단할건지..
# set에 새로운 숫자가 나오면 저장하고, 같은 숫자가 나올 떄까지의 숫자를 다시 저장한다. ex) a, abca -> abc
# set에 들어있는 수가 나오는 경우 다시 시작수가 나올 때까지 비교 ex) a, abda -> abd?

import sys

def isGoodArr(arr):
    arr_length = len(arr)   # 현재 수열 길이
    for part_length in range(1, arr_length // 2 + 1):   # 비교할 수열 길이
        # 부분 수열 비교 시작
        for part_start in range(part_length, arr_length - part_length + 1):
            # 같은 부분 수열을 발견하면
            if arr[(part_start - part_length):part_start] == arr[part_start:(part_start + part_length)]:
                return False			# False 리턴
    # 모든 부분수열이 다르면
    return True

# 백트래킹
def dfs(arr, depth):
    if depth == N:	# 원하는 길이
        print(''.join(map(str, arr)))	# 수열 출력
        sys.exit()				# 종료
    arr.append(1)				# 1 추가 (아무 수나 상관 없음) -> 처음 수를 유지하기 위헤
    for i in range(1, 4):			# 1부터 3까지 반복
        arr.pop()   # 넣었던 수를 빼고 다음 수를 추가(먼저 빼주는 작업이 있어야 다음 수를 넣는게 가능하다. 위의 append를 해야하는 이유)
        arr.append(i)
        if isGoodArr(arr):			# 해당 수열이 좋은 수열이면
            if not dfs(arr, depth + 1):		# 다음 자리 수 시작
            # 만약 다음 자리 수에서 1~3 모두 넣어도 좋은 수열이 없다면 현재 자리수 1 증가
                continue
    # 현재 자리 수 1~3 모두 넣어도 좋은 수열이 없는 경우
    arr.pop()				# 마지막에 넣은 수 없애기
    return False				# False 리턴


N = int(input())
dfs([1], 1)





