from itertools import groupby

s = input()

result = [(int(char), sum(1 for _ in group)) for char, group in groupby(s)]

for item in result:
    print((item[1], item[0]), end=" ")