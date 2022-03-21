# https://www.acmicpc.net/problem/16508
# 완전탐색
# 32432KB, 492ms
# 다시 풀어보기

import sys

T = input()
N = int(input())
costs = []
books = []
for _ in range(N):
    cost, book = input().split(' ')
    costs.append(int(cost))
    books.append(book)


def wordinbook(word, book, price):
    cnt = 0
    for w in word:
        if w in book:
            cnt += 1
            book = book.replace(w, ' ', 1) # 오려낸 글자는 없애준다
            if cnt == len(word):
                return price
    return sys.maxsize  # 시스템이 지정할 수 있는 최댓값

result = []

# 조합 만들기
for i in range(1 << len(books)):
    search_str = ""
    sum_price = 0
    for j in range(len(books)):
        if (i & 1 << j) != 0:
            search_str += books[j]
            sum_price += costs[j]

    result.append(wordinbook(T, search_str, sum_price))

result = min(result)
# 만들 수 없는 경우
if result == sys.maxsize:
    result = -1

print(result)
