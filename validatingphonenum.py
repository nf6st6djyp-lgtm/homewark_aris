import re

n = int(input())
pattern = r'^[789]\d{9}$'

for _ in range(n):
    s = input().strip()
    if re.match(pattern, s):
        print("YES")
    else:
        print("NO")
