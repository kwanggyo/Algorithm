# p, q, r 위치에서의 a값들을 구하여
#  print(p, q, r) 에서
#  p, q, r 을 대신하여 작성한다.

from datetime import datetime

now = datetime.now()
a = 0
a = now.year - 1900  # p
p = a
a += now.month - 1  # q
q = a
a += now.day
r = a
print(p, q, r)

# 실패 -> 문제를 이해 못함