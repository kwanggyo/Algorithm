Min_h, Min_w = map(int, input().split())
Ki_h, Ki_w = map(int, input().split())
if Min_h > Ki_h and Min_w > Ki_w:
    print(1)
else:
    print(0)

# 4MB, 78ms