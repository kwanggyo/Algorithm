A, B, C = map(int, input().split())

if A > B and A > C:
    large = 1
else:
    large = 0
if A == B == C:
    same = 1
else:
    same = 0
print(f'{large} {same}')

# 4MB, 79ms