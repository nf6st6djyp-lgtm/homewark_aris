n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    cmd, _ = input().split()
    other = set(map(int, input().split()))
    getattr(s, cmd)(other)
print(sum(s))
