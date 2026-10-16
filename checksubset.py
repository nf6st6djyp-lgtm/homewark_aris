t = int(input())
for _ in range(t):
    n = int(input())
    a = set(input().split())
    m = int(input())
    b = set(input().split())
    print(a.issubset(b))