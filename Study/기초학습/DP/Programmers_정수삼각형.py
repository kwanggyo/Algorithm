# https://programmers.co.kr/learn/courses/30/lessons/43105
# DP

def solution(triangle):
    # 위에서 부터 각 인덱스에 맞는 값을 더해준다.
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            # 예외 처리
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            # 예외 처리
            elif j == i:
                triangle[i][j] += triangle[i - 1][j -1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    answer = max(triangle[-1])
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))