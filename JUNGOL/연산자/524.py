A, B = map(int, input().split())
if A and B:
    C_and = 1
else:
    C_and = 0
if A or B:
    C_or = 1
else:
    C_or = 0
print(f'{C_and} {C_or}')

# 4MB, 89ms