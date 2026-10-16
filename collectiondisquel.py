from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    cmd = input().split()
    if len(cmd) == 2:
        getattr(d, cmd[0])(cmd[1])
    else:
        getattr(d, cmd[0])()

print(" ".join(d))
