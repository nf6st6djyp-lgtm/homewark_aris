n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    parts = input().split()
    cmd = parts[0]
    if cmd == "pop":
        s.remove(min(s))
    elif cmd == "remove":
        x = int(parts[1])
        s.remove(x)
    elif cmd == "discard":
        x = int(parts[1])
        s.discard(x)
print(sum(s))
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    parts = input().split()
    cmd = parts[0]
    if cmd == "pop":
        s.remove(min(s))
    elif cmd == "remove":
        x = int(parts[1])
        s.remove(x)
    elif cmd == "discard":
        x = int(parts[1])
        s.discard(x)
print(sum(s))
