a, b, c = map(float, input().split())
sum = int(a) + int(b) + int(c)
# avg = (a + b + c) / 3       # {:.0f} 4MB 80 ms 40점
avg = int(a + b + c) // 3
print('sum {}'.format(sum))
print('avg {}'.format(avg))

# 4MB 76ms