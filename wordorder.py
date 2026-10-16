from collections import OrderedDict

n = int(input())
counts = OrderedDict()

for _ in range(n):
    word = input().strip()
    counts[word] = counts.get(word, 0) + 1

print(len(counts))
print(" ".join(str(count) for count in counts.values()))

