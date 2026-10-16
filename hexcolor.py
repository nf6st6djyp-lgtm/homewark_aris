import re

n = int(input())
lines = [input() for _ in range(n)]

pattern = r'(?<=[:\s])#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b'

for line in lines:
    matches = re.findall(pattern, line)
    for match in matches:
        print(match)