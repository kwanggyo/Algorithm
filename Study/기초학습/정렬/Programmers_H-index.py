# https://programmers.co.kr/learn/courses/30/lessons/42747
# 정렬
# 오름차순으로 정렬한 후 인덱스와 값을 비교한다.
# 값이 [전체길이 - 인덱스] 보다 크거나 같으면 정답 = 전체길이 - 인덱스

# def solution(citations):
#     answer = 0
#     citations.sort()
#     for idx, citation in enumerate(citations):
#         if citation >= len(citations) - idx:
#             answer = len(citations) - idx
#             return answer
#     return answer



# # 내림차순 풀이
# def solution(citations):
#     citations.sort(reverse=True)
#     for idx , citation in enumerate(citations):
#         if idx >= citation:
#             return idx
#     return len(citations)



# # 풀이 참고...
# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer

