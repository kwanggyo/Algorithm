# https://programmers.co.kr/learn/courses/30/lessons/42577
# 해시

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer


### 정확성 83.3, 효율성 8.3 = 91.7/100 코드
# def solution(phone_book):
#     answer = True
#     # phone_book.sort() # 없어도 통과
#     # 길이순으로 정렬해서 앞에서부터 검사가 가능하도록 한다.
#     phone_book.sort(key = lambda x : len(x))
#
#     for i in range(len(phone_book)):
#         if answer == False:
#             break
#
#         for j in range(i + 1, len(phone_book)):
#             # 앞에서부터 글자수만큼 검사해서 일치하는지 판단
#             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                 answer = False
#                 break
#
#     return answer


### 다른 정답 풀이 -> startswitch 사용
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True


## zip 함수
# print(list(zip([1,2,3], (4,5,6), "abcd")))
### [[1, 4, 'a'], [2, 5, 'b'], [3, 6, 'c']]

## startswith 함수
# print("dfagd".startswith("abcd"))
# print("abcde".startswith("abcd"))
### False
### True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))